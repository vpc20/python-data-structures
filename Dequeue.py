from Queues import Queue


class Dequeue(Queue):
    def peek_back(self):
        return self.back.data if self.back else None


dq = Dequeue()
print('asdfasd')
print(dq.peek_back())
print(dq.peek_back())
print(dq.peek_back())
dq.enqueue(1)
dq.enqueue(2)
print(dq.peek_back())
