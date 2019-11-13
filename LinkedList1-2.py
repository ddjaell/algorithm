"""
LinkedList 구현
"""


class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print("Linkedlist가 비어있습니다.")
            return

        if self.head == data:
            node = self.head
            self.head = node.next
            del node
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next




linkedlist1 = NodeMgmt(0)
# linkedlist1.desc()

for i in range(1, 10):
    linkedlist1.add(i)


linkedlist1.delete(2)
linkedlist1.delete(9)
linkedlist1.delete(0)
linkedlist1.desc()


