from collections import deque

q = deque()
print(q)

# Enqueue - Add an element to the right - O(1)
q.append(5)
q.append(6)
q.append(7)
q.append(8)

print(q)

# Deque (pop left) - Remove element from the left O(1)
q.popleft()
print(q)

# Peek from left side - O(1)
print(q[0])

# Peek from the right side - O(1
print(q[-1])


