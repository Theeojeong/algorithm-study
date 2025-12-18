class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self.head is None


stack = Stack()
print(stack.push(4))
print(stack.push(3))
print(stack.push(2))
print(stack.head.data)
print(stack.head)

