# https://martinheinz.dev/blog/52
import more_itertools

# divide - divides iterable into number of sub-iterables
# the length of the sub-iterables might not be the same, as it depends on number of elements being divided and number of sub-iterables
data = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]

div_data = [list(l) for l in more_itertools.divide(3, data)] #  [['first', 'second', 'third'], ['fourth', 'fifth'], ['sixth', 'seventh']] 
print(div_data)

data = [5,6,7,8,9,10]

div_data = [list(l) for l in more_itertools.divide(3, data)] #  [['first', 'second', 'third'], ['fourth', 'fifth'], ['sixth', 'seventh']] 
print(div_data)

# There is one more similar function in more_itertools called `distribute`, it however doesn't maintain order. 
# If you don't care about order you should use distribute as it needs less memory.

# partition - divide iterable using a predicate

# Split based on age - splitting list of dates into recent ones and old ones
from datetime import datetime, timedelta

dates = [
    datetime(2015, 1, 15),
    datetime(2025, 1, 16),
    datetime(2025, 1, 17),
    datetime(2019, 2, 1),
    datetime(2025, 2, 2),
    datetime(2018, 2, 4)
]

is_old = lambda x: datetime.now() - x < timedelta(days=30)

old, recent = more_itertools.partition(is_old, dates) # pass function that performes the perdicate and data to be partitioned
print(list(old))
#  [datetime.datetime(2015, 1, 15, 0, 0), datetime.datetime(2019, 2, 1, 0, 0), datetime.datetime(2018, 2, 4, 0, 0)]
print(list(recent))
#  [datetime.datetime(2025, 1, 16, 0, 0), datetime.datetime(2025, 1, 17, 0, 0), datetime.datetime(2025, 2, 2, 0, 0)]

# Split based on file extension - partitioning files based on their extension. 
# Spliting file name into name and extension and checks whether the extension is in list of allowed ones
files = [
    "foo.jpg",
    "bar.exe",
    "baz.gif",
    "text.txt",
    "data.bin",
]

ALLOWED_EXTENSIONS = ('jpg','jpeg','gif','bmp','png')
is_allowed = lambda x: x.split(".")[1] in ALLOWED_EXTENSIONS

allowed, forbidden = more_itertools.partition(is_allowed, files)
print(list(allowed)) #  ['bar.exe', 'text.txt', 'data.bin']
print(list(forbidden)) #  ['foo.jpg', 'baz.gif']

# consecutive_groups - find runs of consecutive numbers, dates, letters, booleans or any other orderable objects
dates = [
    datetime(2020, 1, 15),
    datetime(2020, 1, 16),
    datetime(2020, 1, 17),
    datetime(2020, 2, 1),
    datetime(2020, 2, 2),
    datetime(2020, 2, 4)
]

ordinal_dates = []
for d in dates:
    ordinal_dates.append(d.toordinal()) # convert date to ordinal

groups = [list(map(datetime.fromordinal, group)) for group in more_itertools.consecutive_groups(ordinal_dates)]
print(groups)

# In this example, we have list of dates, where some of them are consecutive. 
# To be able to pass these dates to consecutive_groups function, we first have to convert them to ordinal numbers. 
# Then using list comprehension we iterate over groups of consecutive ordinal dates created by consecutive_groups and convert them back to `datetime` using `map` and `fromordinal` functions.

# collapse - flatten multiple levels of nesting, allows base type & levels specification to stop flattening with one layer of lists/tuples remaining.

# Get flat list of all files and directories in the parent folder
import os
list(more_itertools.collapse(list(os.walk("../"))))

# Get all nodes of tree into flat list
tree = [40, [25, [10, 3, 17], [32, 30, 38]], [78, 50, 93]]  # [Root, SUB_TREE_1, SUB_TREE_2, ..., SUB_TREE_n]
flattened_tree = list(more_itertools.collapse(tree))
print(flattened_tree)

tree = [40, [25, [10, [3, 17]], [32, [30], 38]], [78, 50, 93]]
flattened_tree_2 = list(more_itertools.collapse(tree, levels=2))
print(flattened_tree_2)

# split_at - splits iterable into lists based on predicate. 
# This works like basic split for strings, but here we have iterable instead of string and predicate function instead of delimiter

lines = [
    "erhgedrgh",
    "erhgedrghed",
    "esdrhesdresr",
    "ktguygkyuk",
    "-------------",
    "srdthsrdt",
    "waefawef",
    "ryjrtyfj",
    "-------------",
    "edthedt",
    "awefawe",
]

split_lines = list(more_itertools.split_at(lines, lambda x: '-------------' in x))
print(split_lines) # #  [['erhgedrgh', 'erhgedrghed', 'esdrhesdresr', 'ktguygkyuk'], ['srdthsrdt', 'waefawef', 'ryjrtyfj'], ['edthedt', 'awefawe']]

# bucket - split iterable into multiple buckets based on some condition, creates child iterables by splitting input iterable using key function

# bucket iterable based on items type
class Cube:
    def __repr__(cls):
        return "Cube"

class Circle:
    def __repr__(cls):
        return "Circle"

class Triangle:
    def __repr__(cls):
        return "Triangle"

shapes = [Circle(), Cube(), Circle(), Circle(), Cube(), Triangle(), Triangle()]
s = more_itertools.bucket(shapes, key=lambda x: type(x)) # creates a bucket object
print(list(s))

cube_bucket = list(s[Cube]) # object supports lookup like built-in dict
print(cube_bucket)

circle_bucket = list(s[Circle])
print(circle_bucket)


# map_reduce - specify 3 functions: key function (for categorizing), value function (for transforming) and reduce function (for reducing)

data = 'This sentence has words of various lengths in it, both short ones and long ones'.split()

keyfunc = lambda x: len(x)
result = more_itertools.map_reduce(data, keyfunc)
print(result)
# defaultdict(None, {
#   4: ['This', 'both', 'ones', 'long', 'ones'],
#   8: ['sentence'],
#   3: ['has', 'it,', 'and'],
#   5: ['words', 'short'],
#   2: ['of', 'in'],
#   7: ['various', 'lengths']})

valuefunc = lambda x: 1
result = more_itertools.map_reduce(data, keyfunc, valuefunc)
print(result)
# defaultdict(None, {
#   4: [1, 1, 1, 1, 1],
#   8: [1],
#   3: [1, 1, 1],
#   5: [1, 1],
#   2: [1, 1],
#   7: [1, 1]})

reducefunc = sum
result = more_itertools.map_reduce(data, keyfunc, valuefunc, reducefunc)
print(result)
# defaultdict(None, {
#   4: 5,
#   8: 1,
#   3: 3,
#   5: 2,
#   2: 2,
#   7: 2})

# sort_together - specify by which column(s) to sort the data

cols = [
    ("John", "Ben", "Andy", "Mary"),
    ("1994-02-06", "1985-04-01", "2000-06-25", "1998-03-14"),
    ("2020-01-06", "2019-03-07", "2020-01-08", "2018-08-15")
]

sorted_cols = more_itertools.sort_together(cols, key_list=(1, 2))
print(sorted_cols)
#  [('Ben', 'John', 'Mary', 'Andy'), ('1985-04-01', '1994-02-06', '1998-03-14', '2000-06-25'), ('2019-03-07', '2020-01-06', '2018-08-15', '2020-01-08')]

# Input to the function is list of iterables (columns) and `key_list` which is tells `sort_together` which of the iterables to use for sorting and with what priority. 
# In case of the above example with first sort the "table" by Date of Birth and then by Updated At column.

# seekable - function that wraps iterable in object that makes it possible to go back and forth through iterator, even after some elements were consumed

data = "This is example sentence for seeking back and forth".split()

it = more_itertools.seekable(data)
for word in it:
    print(word)

# next(it) # StopIteration
it.seek(3)
print(next(it)) # "sentence"

# we've got `StopIteration` exception after going through whole iterator, but we can seek back and keep working with it.

# filter_except - filters items of input iterable, by passing elements of iterable to provided function and checking whether 
# it throws error (TypeError, ValueError) or not, keeping only elements that passed the check

data = ['1.5', '6', 'not-important', '11', '1.23E-7', 'remove-me', '25', 'trash']
filtered_data = list(map(float, more_itertools.filter_except(float, data, TypeError, ValueError)))
print(filtered_data)

# unique_to_each - takes bunch of iterables and returns elements from each of them, that aren't in the other ones (mutually exclusive)

graph = {'A': {'B', 'E'}, 'B': {'A', 'C'}, 'C': {'B'}, 'D': {'E'}, 'E': {'A', 'D'}}

filtered_graph = more_itertools.unique_to_each({'B', 'E'}, {'A', 'C'}, {'B'}, {'E'}, {'A', 'D'})
print(filtered_graph) # [[], ['C'], [], [], ['D']]

# If we discard B node, then C gets isolated and if we discard E node, then D gets isolated
# we define graph data structure using adjacency list (actually dict). We then pass neighbours of each node as a set to unique_to_each. 
# What it outputs is a list of nodes that would get isolated if respective node was to be removed.

# numeric_range - iterate over range of some non-integer values
import datetime

num_range = list(more_itertools.numeric_range(1.7, 3.5, 0.3))
print(num_range) # [1.7, 2.0, 2.3, 2.6, 2.9, 3.2]

start = datetime.datetime(2020, 2, 10)
stop = datetime.datetime(2020, 2, 15)
step = datetime.timedelta(days=2)
daterange = list(more_itertools.numeric_range(start, stop, step))
print(daterange) #  [datetime.datetime(2020, 2, 10, 0, 0), datetime.datetime(2020, 2, 12, 0, 0), datetime.datetime(2020, 2, 14, 0, 0)]

# make_decorator - use other itertools as decorators and therefore modify outputs of other functions, producing iterators

mapper_except = more_itertools.make_decorator(more_itertools.map_except, result_index=1)

@mapper_except(float, ValueError, TypeError)
def read_file(f):
    ... # Read mix of text and numbers from file
    return ['1.5', '6', 'not-important', '11', '1.23E-7', 'remove-me', '25', 'trash']

result = list(read_file("file.txt"))
print(result) # [1.5, 6.0, 11.0, 1.23e-07, 25.0]

# This example takes map_except function and creates decorator out of it.
# This decorator will consume result of decorated function as its second argument (result_index=1). 
# In our case, the decorated function is read_file, which simulates reading data of some file and outputs list of strings that might or might not be floats. 
# The output however, is first passed to decorator, which maps and filters all the undesirable items, leaving us with only floats.