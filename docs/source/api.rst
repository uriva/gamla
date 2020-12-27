API
===

currying
--------

.. currentmodule:: gamla.currying

.. autosummary::
   curry

data
----

.. currentmodule:: gamla.data

.. autosummary::
   freeze_deep
   get_encode_config
   match
   tuple_of_tuples_to_csv

functional
----------

.. currentmodule:: gamla.functional

.. autosummary::
   add
   add_key_value
   apply
   assert_that
   assoc_in
   attrgetter
   bottom
   concat_with
   contains
   count
   curried_map_sync
   dataclass_replace
   dataclass_transform
   divide_by
   do_if
   drop
   drop_last_while
   eq_by
   eq_str_ignore_case
   equals
   frequencies
   get_all_n_grams
   get_in
   get_in_or_none
   get_in_or_none_uncurried
   get_in_with_default
   greater_equals
   greater_than
   groupby_many_reduce
   head
   identity
   ignore_input
   inside
   interpose
   invoke
   is_instance
   itemgetter
   itemgetter_or_none
   itemgetter_with_default
   just
   just_raise
   last
   len_equals
   len_greater
   len_smaller
   less_equals
   less_than
   log_text
   make_call_key
   make_raise
   multiply
   not_equals
   nth
   pack
   partition_after
   partition_before
   pmap
   prefix
   profileit
   reduce
   remove_key
   sample
   second
   singleize
   skip
   sort
   sort_by
   sort_by_reversed
   sort_reversed
   star
   suffix
   tail
   take
   take_last_while
   take_while
   to_json
   top
   translate_exception
   unique
   unique_by
   update_in
   wrap_dict
   wrap_str
   wrap_tuple
   wrapped_partial

functional_async
----------------

.. currentmodule:: gamla.functional_async

.. autosummary::
   aconcat
   aexcepts
   afirst
   amap_ascompleted
   mapa
   run_sync

functional_generic
------------------

.. currentmodule:: gamla.functional_generic

.. autosummary::
   after
   alljuxt
   allmap
   anyjuxt
   anymap
   apply_spec
   average
   before
   bifurcate
   case
   case_dict
   check
   complement
   compose
   compose_left
   compose_many_to_one
   compose_sync
   countby_many
   curried_filter
   curried_map
   curried_ternary
   curried_to_binary
   find
   find_index
   first
   groupby
   itemfilter
   itemmap
   juxt
   juxtcat
   keyfilter
   keymap
   lazyjuxt
   map_dict
   map_filter_empty
   mapcat
   merge
   merge_with
   pair_right
   pair_with
   pipe
   reduce_curried
   remove
   stack
   ternary
   to_awaitable
   unless
   valfilter
   valmap
   value_to_dict
   when

graph
-----

.. currentmodule:: gamla.graph

.. autosummary::
   graph_traverse
   graph_traverse_many
   general_graph_traverse_many
   traverse_graph_by_radius
   edges_to_graph
   graph_to_edges
   reverse_graph
   cliques_to_graph
   get_connectivity_components
   groupby_many
   has_cycle

graph_async
-----------
.. currentmodule:: gamla.graph_async

.. autosummary::
   agraph_traverse
   agraph_traverse_many
   agroupby_many
   atraverse_graph_by_radius

io_utils
--------

.. currentmodule:: gamla.io_utils

.. autosummary::
   batch_calls
   get_async
   post_json_async
   post_json_with_extra_headers_async
   queue_identical_calls
   requests_with_retry
   throttle
   timeit
   timeout

string_utils
------------

.. currentmodule:: gamla.string_utils

.. autosummary::
   replace_in_text
   split_in_text


transducer
--------

.. currentmodule:: gamla.transducer

.. autosummary::
   apply_spec
   concat
   count_by
   filter
   groupby
   groupby_many
   juxt
   map
   mapcat
   transduce

tree
----

.. currentmodule:: gamla.tree

.. autosummary::
   filter_leaves
   get_leaves_by_ancestor_predicate


Definitions
-----------

.. automodule:: gamla.__init__
   :members:

.. automodule:: gamla.currying
   :members:

.. automodule:: gamla.data
   :members:

.. automodule:: gamla.functional
   :members:

.. automodule:: gamla.functional_async
   :members:

.. automodule:: gamla.functional_generic
   :members:

.. automodule:: gamla.graph
   :members:

.. automodule:: gamla.graph_async
   :members:

.. automodule:: gamla.io_utils
   :members:

.. automodule:: gamla.string
   :members:

.. automodule:: gamla.transducer
   :members:

.. automodule:: gamla.tree
   :members:
