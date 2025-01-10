# https://docs.python.org/3/library/functools.html
from functools import *

# map - Return an iterator that applies function to every item of iterable, yielding the results. 
# If additional iterables arguments are passed, function must take that many arguments and is applied 
# to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. 

# map(function, iterable, *iterables)

maped_iter = map(iter, ['ABC', 'D', 'EF'])
for i in maped_iter:
    for j in i:
        print(j)

next(next(maped_iter))

# @cache - unbounded function cache, wrapper around a dictionary lookup for the function arguments.
@cache 
def factorial(n):
    return n * factorial(n-1) if n else 1   # returns 1 if n == 0 

factorial(10)      # no previously cached result, makes 11 recursive calls
factorial(5)       # just looks up cached value result
factorial(12)      # makes two new recursive calls, the other 10 are cached

# cmp_to_key - Transform an comparison function to a key function
# Used with tools that accept key functions (such as sorted(), min(), max(), heapq.nlargest(), heapq.nsmallest(), itertools.groupby())

