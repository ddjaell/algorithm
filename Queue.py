import queue
from random import *
"""
일반 큐 first in first out
"""
normal_q = queue.Queue()
normal_q.put(1111)
for i in range(10):
    normal_q.put(i)
print("-----FIFO queue 출력---------")
for i in range(normal_q.qsize()):
    print(normal_q.get(), end=' ')
print()

"""
LIFO 큐
"""
lifo_q = queue.LifoQueue()
lifo_q.put(111111)
for i in range(10):
    lifo_q.put(i)
print("-----LIFO queue 출력---------")
for i in range(lifo_q.qsize()):
    print(lifo_q.get(), end=' ')
print()

"""
priority 큐
"""
p_q = queue.PriorityQueue()
p_q.put(111111, 101)
for i in range(10):
    p_q.put(i, randint(1, 100))
print("-----Priority queue 출력---------")
for i in range(p_q.qsize()):
    print(p_q.get(), end=' ')


"""
큐를 리스트로 만들기
"""

list_q = list()

def enq(data):

    list_q.append(data)


def deq():

    data = list_q[0]
    del list_q[0]
    return data

def size():

    return len(list_q)


print()

print("list_q의 사이즈는 : ", size())

for i in range(5):

    enq(i)

print("enq 후 list_q의 사이즈는 : ", size())

for i in range(5):

    print(deq())

print("deq 후 list_q의 사이즈는 : ", size())




