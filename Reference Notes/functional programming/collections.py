# Collections - implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.
# https://docs.python.org/3/library/collections.html

# namedtuple - assign meaning to each position in a tuple and allow for more readable, self-documenting code. 
# They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(x=11, y=22)   # instantiate with positional or keyword arguments
p[0] + p[1]             # indexable like the plain tuple (11, 22)

x, y = p                # unpack like a regular tuple
x, y

p.x + p.y               # fields also accessible by name

p                       # readable __repr__ with a name=value style

# In addition to the methods inherited from tuples, named tuples support three additional methods and two attributes.
# ._make(iterable)
# ._asdict()
# ._replace()
# ._fields
# ._field_defaults

# ._make(iterable) - makes a new instance from an existing sequence or iterable
t = [11, 22]
p_t = Point._make(t)
p_t

# ._asdict() - return a new dict which maps field names to their corresponding values
p = Point(x=11, y=22)
p._asdict()

# ._replace() - return a new instance of the named tuple replacing specified fields with new values
p = Point(x=11, y=22)
p._replace(x=33)

# _fields - Tuple of strings listing the field names
p._fields            # view the field names

Color = namedtuple('Color', 'red green blue')
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
Pixel(11, 22, 128, 255, 0)

# ._field_defaults - Dictionary mapping field names to default values
Account = namedtuple('Account', ['type', 'balance'], defaults=[0]) # defaults are applied to the rightmost parameters
Account._field_defaults
Account('premium')

tab = namedtuple('Tab', ['x', 'y', 'z'], defaults=(1,2)) # x will be a required argument, y will default to 1, and z will default to 2.
tab._field_defaults


# To retrieve a field whose name is stored in a string, use the getattr() function:
getattr(p, 'x')

# To convert a dictionary to a named tuple, use the double-star-operator
d = {'x': 11, 'y': 22}
Point(**d)

# Since a named tuple is a regular Python class, it is easy to add or change functionality with a subclass. 
# Here is how to add a calculated field and a fixed-width print format:
class Point(namedtuple('Point', ['x', 'y'])):
    __slots__ = ()  #  sets __slots__ to an empty tuple. This helps keep memory requirements low by preventing the creation of instance dictionaries.
    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

for p in Point(3, 4), Point(14, 5/7):
    print(p)


# deque - generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). 
# Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

# class collections.deque([iterable[, maxlen]])

# If `maxlen` is not specified or is None, deques may grow to an arbitrary length. 
# Otherwise, the deque is bounded to the specified maximum length. 
# Once a bounded length deque is full, when new items are added, a corresponding number of items are discarded from the opposite end.
# They are also useful for tracking transactions and other pools of data where only the most recent activity is of interest.

# Deque objects support the following methods:
# append(x) - Add x to the right side of the deque.
# appendleft(x) - Add x to the left side of the deque.
# clear() - Remove all elements from the deque leaving it with length 0.
# copy() - Create a shallow copy of the deque.
# count(x) - Count the number of deque elements equal to x.
# extend(iterable) - Extend the right side of the deque by appending elements from the iterable argument.
# extendleft(iterable) - Extend the left side of the deque by appending elements from iterable. Note, the series of left appends results in reversing the order of elements in the iterable argument.
# index(x[, start[, stop]]) - Return the position of x in the deque (at or after index start and before index stop). Returns the first match or raises ValueError if not found.
# insert(i, x) - Insert x into the deque at position i. If the insertion would cause a bounded deque to grow beyond maxlen, an IndexError is raised.
# pop() - Remove and return an element from the right side of the deque.
# popleft() - Remove and return an element from the left side of the deque. 
# remove(value) - Remove the first occurrence of value.
# reverse() - Reverse the elements of the deque in-place and then return None.
# rotate(n=1) - Rotate the deque n steps to the right. If n is negative, rotate to the left. Rotating one step to the right is equivalent to d.appendleft(d.pop()), and rotating one step to the left is equivalent to d.append(d.popleft()).
# maxlen - Maximum size of a deque or None if unbounded.

# In addition to the above, deques support iteration, pickling, `len(d)`, `reversed(d)`, `copy.copy(d)`, `copy.deepcopy(d)`, 
# membership testing with the `in` operator, and subscript references such as d[0] to access the first element. 
# Indexed access is O(1) at both ends but slows to O(n) in the middle. For fast random access, use lists instead.

# deques support __add__(), __mul__(), and __imul__().

from collections import deque
d = deque('ghi')                 # "ghi" is an iterable pased to the deque initilizer which returns a new object of the deque class referenced by `d` with 3 elements.
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())

d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side

d.pop()                          # return and remove the rightmost item
# 'j'
d.popleft()                      # return and remove the leftmost item
# 'f'
list(d)                          # list the contents of the deque
d[0]                             # peek at leftmost item
# 'g'
d[-1]                            # peek at rightmost item
# 'i'

list(reversed(d))                # list the contents of a deque in reverse
# ['i', 'h', 'g']
'h' in d                         # search the deque
# True
d.extend('jkl')                  # add multiple elements at once
# deque(['g', 'h', 'i', 'j', 'k', 'l'])
d.rotate(1)                      # right rotation
# deque(['l', 'g', 'h', 'i', 'j', 'k'])
d.rotate(-1)                     # left rotation
# deque(['g', 'h', 'i', 'j', 'k', 'l'])
deque(reversed(d))               # make a new deque in reverse order
# deque(['l', 'k', 'j', 'i', 'h', 'g'])
d.clear()                        # empty the deque
# d.pop()                          # cannot pop from an empty deque

d.extendleft('abc')              # extendleft() reverses the input order
# deque(['c', 'b', 'a'])

# Bounded length deques provide functionality similar to the tail filter
def tail(filename, n=10): 
    'Return the last n lines of a file'
    with open(filename) as f:
        return deque(f, n) # Once a bounded length deque is full, when new items are added, a corresponding number of items are discarded from the opposite end.

import itertools
# Maintain a sequence of recently added elements by appending to the right and popping to the left
def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # https://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable) # returns an iterator object of the interable list
    d = deque(itertools.islice(it, n-1)) # slice the first n-1 items from iterable (exhausts the n-1 items) and creates a deque object
    d.appendleft(0) # left append 0 to deque 
    s = sum(d) 
    for elem in it: # `it` starts after the n-1 elements in the parameter list (as they are exhausted from the islice call)
        s += elem - d.popleft() 
        d.append(elem)
        yield s / n

ma = moving_average([40, 30, 50, 46, 39, 44])
print(next(ma))
print(next(ma))
print(next(ma))

# A 'round-robin scheduler' can be implemented with input iterators stored in a deque. 
# Values are yielded from the active iterator in position zero. 
# If that iterator is exhausted, it can be removed with popleft(); otherwise, 
# it can be cycled back to the end with the rotate() method:

def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # https://en.wikipedia.org/wiki/Round-robin_scheduling
    iterators = deque(map(iter, iterables)) # 
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()
            
rr = roundrobin('ABC', 'D', 'EF')
print(next(rr))
print(next(rr))
print(next(rr))
print(next(rr))
print(next(rr))
print(next(rr))

# The rotate() method provides a way to implement deque slicing and deletion. 
# For example, a pure Python implementation of del d[n] relies on the rotate() method to position elements to be popped:

def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

d = deque('abdullah')
delete_nth(d, 3)
print(d)
d.rotate(-4)
print(d)

# To implement deque slicing, use a similar approach applying rotate() to bring a target element to the left side of the deque. 
# Remove old entries with popleft(), add new entries with extend(), and then reverse the rotation. With minor variations on that approach, 
# it is easy to implement Forth style stack manipulations such as `dup`, `drop`, `swap`, `over`, `pick`, `rot`, and `roll`.