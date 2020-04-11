##################################
# Stack implementation using array
##################################


class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return not self.data

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()

    def peek(self):
        if not self.is_empty():
            return self.data[-1]

    def size(self):
        return len(self.data)

    def print_list(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            print('=============== Stack ===============')
            for i in range(len(self.data) - 1, -1, -1):
                print(self.data[i])
            print('=========== end of list ==============')


s1 = Stack()
if s1.is_empty():
    print('stack is empty')
print(s1.pop())
print(s1.peek())
print(s1.size())
s1.print_list()

s1.push('a')
s1.push('b')
s1.push('c')
s1.push('d')
s1.push('e')

s1.print_list()
print('Data at top of stack is ' + s1.peek())
print('The size of stack is ' + str(s1.size()))

print(s1.pop() + ' was popped from stack')
print(s1.pop() + ' was popped from stack')
print(s1.pop() + ' was popped from stack')
print(s1.pop() + ' was popped from stack')
print(s1.pop() + ' was popped from stack')

s1.print_list()
