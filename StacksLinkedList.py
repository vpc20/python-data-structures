class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_key(self):
        return self.data

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return not self.top

    def push(self, data):
        new_node = Node(data)  # prepend to list
        new_node.set_next(self.top)
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            curr = self.top
            next = curr.get_next()
            self.top = next
            return curr.get_key()

    def peek(self):
        return self.top.get_key()

    def print_list(self):
        curr = self.top
        while curr:
            print(curr.get_key())
            curr = curr.get_next()


stack = Stack()

stack.push('aaa')
stack.push('bbb')
stack.push('ccc')
stack.push('ddd')
stack.push('eee')

print('================= Stack ===================')
stack.print_list()
print('=============== end of list ===============')

print(stack.pop() + ' was popped from stack')
print('Top of stack is ' + stack.peek())

print('================= Stack ===================')
stack.print_list()
print('=============== end of list ===============')
