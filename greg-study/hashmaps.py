# Hashmaps - Dictionaries

d = {'greg': 1, 'steve': 2, 'cara': 3}
print(d)

# Add key:val in the dic: O(1)
d['dave'] = 4
print(d)

# Check presence of a kep in a dict: O(1)
if 'greg' in d:
    print(True)

# Check the value corresponding to the key in dict: O(1)
print(d['greg'])

# Loop over the key:val pairs: O(n)
for key, value in d.items():
    print(f"key: {key} / val: {value}")

# Default dict
from collections import defaultdict

default = defaultdict(list)

print(default[2])

# Counter - creates a dict of unique values as key value pairs
from collections import Counter

string = 'aaaaaaaaaaaaccccccccccccbbbbbbbbbbeeeeee'
counter = Counter(string)
print(counter)
