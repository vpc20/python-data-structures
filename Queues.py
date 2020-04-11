class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def __str__(self):
        curr, qstr = self.front, ''
        while curr:
            qstr += str(curr.data) + ' '
            curr = curr.next
        return 'Front ==> ' + qstr if qstr else 'Empty queue'

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node  # first item in queue
        else:
            new_node.prev = self.back
            self.back.next = new_node
        self.back = new_node

    def dequeue(self):
        if self.front is not None:
            front = self.front
            if self.front == self.back:  # only one item left in queue
                self.front = None
                self.back = None
            else:
                front = self.front
                self.front.next.prev = None
                self.front = self.front.next
            del front

    def peek(self):
        return self.front.data if self.front else None

    def length(self):
        curr, list_len = self.front, 0
        while curr:
            list_len += 1
            curr = curr.next
        return list_len

    def to_array(self):
        curr, arr = self.front, []
        while curr:
            arr.append(curr.data)
            curr = curr.next
        return arr


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q)
    print(q.peek())
    print('length ', q.length())
    print(q.to_array())

    q.dequeue()
    print(q)
    print(q.peek())
    q.dequeue()
    print(q)
    print(q.peek())
    q.dequeue()
    print(q)
    print(q.peek())
    q.dequeue()
    print(q.peek())
    print(q)
    q.dequeue()
    print(q)
    print(q.peek())
    print('end of program')
