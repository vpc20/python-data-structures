class Queue:
    def __init__(self):
        self.stack1 = []  # will hold queue in reverse order
        self.stack2 = []

    def is_empty(self):
        return len(self.stack1) == 0
        # return not self.stack1

    def enqueue(self, x):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.is_empty():
            return None
        return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]


if __name__ == '__main__':
    q = Queue()
    q.enqueue(5)
    q.enqueue(9)
    q.enqueue(11)
    print(q.peek())
    print(q.stack1)
    print(q.stack2)

    print(f'dequeue {q.dequeue()}')
    print(q.stack1)
    print(q.stack2)

    print(f'dequeue {q.dequeue()}')
    print(q.stack1)
    print(q.stack2)

    print(f'dequeue {q.dequeue()}')
    print(q.stack1)
    print(q.stack2)

    print(f'dequeue {q.dequeue()}')
    print(q.stack1)
    print(q.stack2)
