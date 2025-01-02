from collections import defaultdict

# Looping over dictionary keys
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

for k in d:
    print(k)
    
for k in list(d.keys()):
    if k.startswith('r'):
        del d[k]

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

d = {k: d[k] for k in d if not k.startswith('r')}

# Construct a dictionary from pairs
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(zip(names, colors))

# Counting with dictionaries
colors = ['red', 'green', 'red', 'blue', 'green', 'red']

d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1

d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
    
d = defaultdict(int)
for color in colors:
    d[color] += 1

# Grouping with dictionaries - 1
names = ['raymond', 'rachel', 'matthew', 'roger', 
         'betty', 'melissa', 'judith', 'charlie']

d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)


# .popitem()
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

while d:
    key, value = d.popitem()
    print(key, '-->' ,value)

