class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_key(self):
        return self.data

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev


class Deque:
    def __init__(self):
        self.front = None
        self.back = None

    def is_empty(self):
        return not self.back

    def enqueue_front(self, data):
        if self.is_empty():
            self.create_first_node(data)
        else:
            new_node = Node(data)
            new_node.set_next(self.front)
            self.front = new_node
            next = new_node.get_next()
            next.set_prev(new_node)

    def enqueue_back(self, data):
        if self.is_empty():
            self.create_first_node(data)
        else:
            curr = self.back
            new_node = Node(data)
            new_node.set_prev(curr)
            curr.set_next(new_node)
            self.back = new_node

    def create_first_node(self, data):
        new_node = Node(data)
        self.front = new_node
        self.back = new_node

    def dequeue_front(self):
        if not self.is_empty():
            curr = self.front
            if curr.get_next() is None:  # only one item in list
                self.front = None
                self.back = None
            else:
                next = curr.get_next()
                self.front = next
                next.set_prev(None)
                curr.set_next(None)
            return curr.get_key()
        else:
            return None

    def dequeue_back(self):
        if not self.is_empty():
            curr = self.back
            if curr.get_prev() is None:  # only 1 item left in the queue
                self.front = None
                self.back = None
            else:
                prev = curr.get_prev()
                self.back = prev
                prev.set_next(None)
                curr.set_prev(None)
            return curr.get_key()
        else:
            return None

    def peek_front(self):
        if not self.is_empty():
            return self.front.get_key()
        else:
            return None

    def peek_back(self):
        if not self.is_empty():
            return self.back.get_key()
        else:
            return None

    def print_list(self):
        curr = self.front
        while curr:
            print(curr.get_key())
            curr = curr.get_next()

    def print_reverse(self):
        curr = self.back
        while curr:
            print(curr.get_key())
            curr = curr.get_prev()


dq = Deque()

dq.enqueue_front('ccc')
dq.enqueue_front('bbb')
dq.enqueue_front('aaa')
dq.enqueue_back('ddd')
dq.enqueue_back('eee')

print('================== Queue ==================')
dq.print_list()
print('=============== end of list ===============')

print(dq.dequeue_front() + ' was removed from front of queue')
# print dq.dequeue_front() + ' was removed from front of queue'
# print dq.dequeue_front() + ' was removed from front of queue'
# print dq.dequeue_front() + ' was removed from front of queue'
# print dq.dequeue_front() + ' was removed from front of queue'

print(dq.dequeue_back() + ' was removed from back of queue')
# print dq.dequeue_back() + ' was removed from back of queue'
# print dq.dequeue_back() + ' was removed from back of queue'
# print dq.dequeue_back() + ' was removed from back of queue'


print('================== Queue ==================')
dq.print_list()
print('=============== end of list ===============')

print('Front of queue is ' + str(dq.peek_front()))
print('Back  of queue is ' + str(dq.peek_back()))

dq.print_reverse()

# print dq.dequeue() + ' was removed from queue'
# print 'Front of queue is ' + dq.peek()
#
# print '================== Queue =================='
# dq.print_list()
# print '=============== end of list ==============='
