# https://docs.python.org/3/library/itertools.html
# https://martinheinz.dev/blog/52

import itertools
import operator

# iter() - built-in function that returns an iterator object (objects that actually perform the iteration on iterables)
# iter(object, sentinel [optional]) 
# 'object' - can be a list, set, tuple, etc.
# 'sentinel [optional]' - a special value that is used to represent the end of a sequence


phones = ['apple', 'samsung', 'oneplus']
phones_iter = iter(phones)

print(next(phones_iter))   
print(next(phones_iter))    
print(next(phones_iter))  
print(next(phones_iter))  

# Output:
# apple
# samsung
# oneplus
# Error: StopIteration


# compress: filtering sequences - takes iterable and boolean selector and outputs items of the iterable where the corresponding element in the selector is True.
dates = [
    "2020-01-01",
    "2020-02-04",
    "2020-02-01",
    "2020-01-24",
    "2020-01-08",
    "2020-02-10",
    "2020-02-15",
    "2020-02-11",
]
counts = [1, 4, 3, 8, 0, 7, 9, 2]
bools = [n > 3 for n in counts] # list of bools indicating position to filter: [False, True, False, True, False, True, True, False]
compressed = list(itertools.compress(dates, bools))
print(compressed) # ['2020-02-04', '2020-01-24', '2020-02-10', '2020-02-15']

values = 'ABCDEF'
bools =  [1,0,1,0,1,1]
compressed = list(itertools.compress(values, bools))
print(compressed) # ['A', 'C', 'E', 'F']

# accumulate - accumulate results of some (binary) function

data = [1,2,3,4,5]
cumsum = list(itertools.accumulate(data)) # perform cumulative sum

data = [3, 4, 1, 3, 5, 6, 9, 0, 1]
running_max = list(itertools.accumulate(data, max)) # running maximum
print(running_max) # returns the maximum value seen at every position of the lists: [3, 4, 4, 4, 5, 6, 9, 9, 9]

cumprod = list(itertools.accumulate(data, operator.mul)) # cumulative product
print(cumprod) # [3, 12, 12, 36, 180, 1080, 9720, 0, 0]

fact = list(itertools.accumulate(range(1, 11), operator.mul))  # Factorial
print(fact) #  [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


# cycle - takes iterable and creates infinite cycle from it

players = ["John", "Ben", "Martin", "Peter"]

next_player = itertools.cycle(players).__next__
player = next_player()
print(player)

for _ in range(5):
    print(next_player())

skiped_players = itertools.islice(itertools.cycle(players), 2, None).__next__ # skipping few elements of iterable (in other words - starting at different element).

print()
for _ in range(7):
    print(skiped_players())
    

# tee - creates multiple iterators from one, which allows us to remember what happened

def pairwise(iterable):
    """
    s -> (s0, s1), (s1, s2), (s2, s3), ...
    """
    a, b = itertools.tee(iterable, 2)
    next(b, None)
    return zip(a, b)

# This function is handy every time you need multiple separate pointers to same stream of data.
# This can be costly when it comes to memory. 
# Do not use original iterable after using tee as it will unintentionally advance those new tee objects.

pairs = pairwise(players)

for i,j in pairs:
    print(i, j)

# islice - Make an iterator that returns selected elements from the iterable. 
# Works like sequence slicing but does not support negative values for start, stop, or step.
# .islice(iterable, start, stop[, step])

# Slicing the range function
for i in itertools.islice(range(20), 5): # iterator with first 5 (stop index) items from the iterable
    print(i)
     
     
li = [2, 4, 5, 7, 8, 10, 20] 
 
# Slicing the list
print(list(itertools.islice(li, 1, 6, 2))) # iterator selecting from the start of the 1st index to the 6th index with 2 steps between each element
