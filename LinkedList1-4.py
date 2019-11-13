"""
LinkedList 구현
"""


class Node:

    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

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




double_linkedlist = NodeMgmt(0)


for i in range(1, 10):
    double_linkedlist.add(i)


double_linkedlist.delete(2)
double_linkedlist.delete(9)
double_linkedlist.delete(0)
double_linkedlist.desc()


