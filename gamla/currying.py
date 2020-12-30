import asyncio
import dataclasses
import functools
import inspect
from typing import Callable


@dataclasses.dataclass
class _Curry:
    function: Callable

    def __call__(self, *args, **kwargs):
        try:
            return self.function(*args, **kwargs)
        except TypeError as e:
            print(f"itay {e}")
            self.function = functools.partial(self.function, *args, **kwargs)
            return self


def curry(f):
    if asyncio.iscoroutinefunction(f):
        return old_curry(f)
    return functools.wraps(f)(_Curry(function=f))


def _curry_helper(
    is_coroutine, f_len_args, f, args_so_far, kwargs_so_far, *args, **kwargs
):
    args_so_far += args
    kwargs_so_far = {**kwargs_so_far, **kwargs}
    len_so_far = len(args_so_far) + len(kwargs_so_far)
    if len_so_far > len(f_len_args):
        return f(*args_so_far)
    if len_so_far == len(f_len_args):
        return f(*args_so_far, **kwargs_so_far)
    if len_so_far + 1 == len(f_len_args) and is_coroutine:

        @functools.wraps(f)
        async def curry_inner_async(*args, **kwargs):
            return await f(*(args_so_far + args), **{**kwargs_so_far, **kwargs})

        return curry_inner_async

    @functools.wraps(f)
    def curry_inner(*args, **kwargs):
        return _curry_helper(
            is_coroutine, f_len_args, f, args_so_far, kwargs_so_far, *args, **kwargs
        )

    return curry_inner


def _infer_defaults(f):
    params = inspect.signature(f).parameters
    kwargs = {}
    for p in params.values():
        if p.default != p.empty:
            kwargs[p.name] = p.default
    return kwargs


def old_curry(f):
    f_len_args = inspect.signature(f).parameters
    assert (
        len(f_len_args) > 1
    ), f"Curry function must have at least 2 parameters, {f} has {len(f_len_args)}"
    defaults = _infer_defaults(f)
    is_coroutine = asyncio.iscoroutinefunction(f)

    @functools.wraps(f)
    def indirection(*args, **kwargs):
        return _curry_helper(is_coroutine, f_len_args, f, (), defaults, *args, **kwargs)

    return indirection


def addition(x):
    return x + 1


def compose(f1, f2):
    def composition(x):
        return f1(f2(x))

    return composition


@curry
def after(f1, f2):
    """Second-order composition of `f1` over `f2`."""
    return compose(f1, f2)


b = after(addition)


def curried_map(f):
    return curried_map_sync(f)


def curried_map_sync(f):
    def curried_map(it):
        for x in it:
            yield f(x)

    return curried_map


map_filter_empty = compose(curried_map, after(curried_map(lambda x: x)))
