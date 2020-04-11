from unittest import TestCase
from Queues import Queue


class TestQueue(TestCase):
    def test_queue(self):
        q = Queue()
        self.assertEqual(None, q.peek())
        self.assertEqual([], q.to_array())

        q.enqueue(1)
        self.assertEqual([1], q.to_array())
        self.assertEqual(1, q.peek())
        q.enqueue(2)
        self.assertEqual([1, 2], q.to_array())
        self.assertEqual(1, q.peek())
        q.enqueue(3)
        self.assertEqual([1, 2, 3], q.to_array())
        self.assertEqual(1, q.peek())
        q.enqueue(4)
        self.assertEqual([1, 2, 3, 4], q.to_array())
        self.assertEqual(1, q.peek())
        q.enqueue(5)
        self.assertEqual([1, 2, 3, 4, 5], q.to_array())
        self.assertEqual(1, q.peek())

        q.dequeue()
        self.assertEqual([2, 3, 4, 5], q.to_array())
        self.assertEqual(2, q.peek())
        q.dequeue()
        self.assertEqual([3, 4, 5], q.to_array())
        self.assertEqual(3, q.peek())
        q.dequeue()
        self.assertEqual([4, 5], q.to_array())
        self.assertEqual(4, q.peek())
        q.dequeue()
        self.assertEqual([5], q.to_array())
        self.assertEqual(5, q.peek())
        q.dequeue()
        self.assertEqual([], q.to_array())
        self.assertEqual(None, q.peek())

