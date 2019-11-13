
"""
파이선은 리스트가 일반리스트와 링크드리스트를 지원한다

"""

""""
링크드리스트 구현, Node 구현 먼저
"""
class Node :

    def __init__(self,data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next= Node(data)



node1 = Node(1)
head = node1
for i in range(2,10):
    add(i)

node = head
while node.next:
    print("현재 노드값 = ",node.data, " 다음 노드 주소 = ", node.next.data)
    node = node.next
print(node.data)



node3 = Node(1.5)
node = head
search = True
while search:
    if node.data ==1:
        search = False
    else:
        node = node.next

tmp = node.next
node.next = node3
node3.next = tmp

while node.next:
    print("현재 노드값 = ",node.data, " 다음 노드 주소 = ", node.next.data)
    node = node.next
print(node.data)



