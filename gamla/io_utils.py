import asyncio
import datetime
import functools
import logging
import time
from typing import Text

import requests
import requests.adapters
from requests.packages.urllib3.util import retry


def _time_to_readable(time_s: float):
    return datetime.datetime.fromtimestamp(time_s)


def _request_id(name, args, kwargs) -> Text:
    args_str = str(args)[:50]
    kwargs_str = str(kwargs)[:50]
    return f"{name}, args: {args_str}, kwargs: {kwargs_str}"


def _async_timeit(f):
    @functools.wraps(f)
    async def wrapper(*args, **kwargs):
        req_id = _request_id(f.__name__, args, kwargs)
        start = time.time()
        logging.info(f"{req_id} started at {_time_to_readable(start)}")
        result = await f(*args, **kwargs)
        finish = time.time()
        elapsed = finish - start
        logging.info(
            f"{req_id} finished at {_time_to_readable(finish)}, took {elapsed}"
        )
        return result

    return wrapper


def timeit(f):
    if asyncio.iscoroutinefunction(f):
        return _async_timeit(f)

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        req_id = _request_id(f.__name__, args, kwargs)
        start = time.time()
        logging.info(f"{req_id} started at {_time_to_readable(start)}")
        result = f(*args, **kwargs)
        finish = time.time()
        elapsed = finish - start
        logging.info(
            f"{req_id} finished at {_time_to_readable(finish)}, took {elapsed}"
        )
        return result

    return wrapper


def requests_with_retry(retries: int = 3) -> requests.Session:
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(
        max_retries=retry.Retry(
            total=retries, backoff_factor=0.1, status_forcelist=(500, 502, 504)
        )
    )
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


# TODO(uri): move the test as well
def batch_calls(f, timeout=20):
    """Batches single call into one request.

    Turns `f`, a function that gets a `tuple` of independent requests, into a function
    that gets a single request.
    """
    queue = {}
    active = False

    async def make_call():
        if not queue:
            await asyncio.sleep(0.1)
            asyncio.create_task(make_call())
            return
        queue_copy = dict(queue)
        queue.clear()
        try:
            for async_result, result in zip(
                queue_copy.values(), await f(tuple(queue_copy))
            ):
                async_result.set_result(result)
        except Exception as exception:
            for async_result in queue_copy.values():
                async_result.set_exception(exception)
        await asyncio.sleep(0.1)
        asyncio.create_task(make_call())

    async def wrapped(hashable_input):
        nonlocal active
        if not active:
            active = True
            asyncio.create_task(make_call())
        if hashable_input in queue:
            return await asyncio.wait_for(queue[hashable_input], timeout=timeout)
        async_result = asyncio.Future()
        # Check again because of context switch due to the creation of `asyncio.Future`.
        # TODO(uri): Make sure this is needed.
        if hashable_input in queue:
            return await asyncio.wait_for(queue[hashable_input], timeout=timeout)
        queue[hashable_input] = async_result
        return await asyncio.wait_for(async_result, timeout=timeout)

    return wrapped
