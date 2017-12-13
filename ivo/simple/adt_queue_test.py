#! /bin/python3

from queue import Queue

q = Queue()

if q.isEmpty():
    print('ok')

q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
