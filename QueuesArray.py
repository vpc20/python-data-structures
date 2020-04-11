##################################
# Queue implementation using array
##################################


class Queue:
    def __init__(self):
        self.q = []

    def is_empty(self):
        return not self.q

    def enqueue(self, data):
        self.q.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.q.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.q[0]

    def size(self):
        return len(self.q)

    def print_list(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            print('Queue ==> ', end='')
            for item in self.q:
                print(item, end=' ')
            print('')


q1 = Queue()
q1.dequeue()
q1.print_list()
print('Front of queue is ' + str(q1.peek()))
print('Size of queue is ' + str(q1.size()))

q1.enqueue('a')
q1.enqueue('b')
q1.enqueue('c')
q1.enqueue('d')
q1.enqueue('e')

q1.print_list()
print('Front of queue is ' + str(q1.peek()))
print('Size of queue is ' + str(q1.size()))

print(q1.dequeue() + ' was removed from queue')
print(q1.dequeue() + ' was removed from queue')
print(q1.dequeue() + ' was removed from queue')

q1.print_list()
print('Front of queue is ' + str(q1.peek()))
print('Size of queue is ' + str(q1.size()))
