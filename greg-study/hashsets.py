# Hashsets

s = set()
print(s)

# Add item into Set - O(1)
s.add(1)
s.add(2)
s.add(3)
print(s)

# Lookup item in set - O(1)
if 1 in s:
    print(True)

# Delete item in set - O(1)
s.remove(3)
print(s)

# Set construction - O(S) - S is the length of the string
# This is also (n) as the set needs to iterate over the string to extract the unique values
# O(s) is sometimes used in place of O(n) to represent a str length
string = 'aaaaaaaaaaaaccccccccccccbbbbbbbbbbeeeeee'
sett = set(string)
print(sett)