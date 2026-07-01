# Stack

stk = []
print(stk)

# Append to the top of the stack - O(1)
stk.append(5)
stk.append(4)
stk.append(3)
stk.append(2)

print(stk)

#  Pop from the stack - O(1)
x = stk.pop()

print(x)
print(stk)

# Ask if something is in the stack - O(1)
if stk:
    print(True)