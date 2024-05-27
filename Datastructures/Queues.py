# FIFO- first in first out
from collections import deque
q = deque([])
q.append(1)
q.append(2)
q.append(3)
print(q)
q.popleft()
print(q)
if q:
    q.popleft()
else:
    print("empty quque")
q.popleft()
print(q)
