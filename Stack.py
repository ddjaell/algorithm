"""
스택은 LIFO, FILO의 형태가 있다
"""

"""
python의 list는 기본적으로 스택의 구조를 가지고 있음
"""
stack_list = list()
stack_list.append(1)
stack_list.append(2)
stack_list.append(3)
print(stack_list)

print(stack_list.pop())
print("after pop() once = ", stack_list)



"""
pop(), push() 함수 만들어보기
"""
stack_self = list()

def push(data):
    stack_self.append(data)

def pop():
    tmp = stack_self[-1]
    del stack_self[-1]
    print(tmp)


for i in range(10):
    push(i)

pop()