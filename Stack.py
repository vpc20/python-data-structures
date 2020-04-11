class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        curr, stck = self.top, ''
        while curr:
            stck += str(curr.data) + ' '
            curr = curr.next
        return stck + '<== Top ' if stck else 'Empty stack'

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is not None:
            top = self.top
            data = self.top.data
            self.top = self.top.next
            del top
            return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def to_array(self):
        curr, arr = self.top, []
        while curr:
            arr.append(curr.data)
            curr = curr.next
        return arr


if __name__ == '__main__':
    stack = Stack()
    print(stack)
    print(stack.peek())

    stack.push(1)
    print(stack)
    print(stack.peek())
    stack.push(2)
    print(stack)
    print(stack.peek())
    stack.push(3)
    print(stack)
    print(stack.peek())
    stack.push(4)
    print(stack)
    print(stack.peek())
    stack.push(5)
    print(stack)
    print(stack.peek())

    print(stack.to_array())

    print(stack.pop())
    print(stack)
    print(stack.peek())
    print(stack.pop())
    print(stack)
    print(stack.peek())
    print(stack.pop())
    print(stack)
    print(stack.peek())
    print(stack.pop())
    print(stack)
    print(stack.peek())
    print(stack.pop())
    print(stack)
    print(stack.peek())
