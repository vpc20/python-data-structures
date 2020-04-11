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


class Queue:
    def __init__(self):
        self.front = None

    def is_empty(self):
        return not self.front

    def enqueue(self, data):
        if self.is_empty():
            new_node = Node(data)  # first item in list
            new_node.set_next(self.front)
            self.front = new_node
            return

        curr = self.front
        while curr:
            if curr.get_next() is None:
                new_node = Node(data)  # append item to end of list
                curr.set_next(new_node)
                break
            curr = curr.get_next()

    def dequeue(self):
        if not self.is_empty():
            curr = self.front
            if curr.get_next() is None:  # only 1 item left in the queue
                self.front = None
                return
            self.front = curr.get_next()
            return curr.get_key()

    def peek(self):
        return self.front.get_key()

    def print_list(self):
        curr = self.front
        while curr:
            print(curr.get_key())
            curr = curr.get_next()


q = Queue()

q.enqueue('aaa')
q.enqueue('bbb')
q.enqueue('ccc')
q.enqueue('ddd')
q.enqueue('eee')

print('================== Queue ==================')
q.print_list()
print('=============== end of list ===============')

print(q.dequeue() + ' was removed from queue')
print('Front of queue is ' + q.peek())

print('================== Queue ==================')
q.print_list()
print('=============== end of list ===============')
