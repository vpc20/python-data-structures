from unittest import TestCase

from Stack import Stack


class TestStack(TestCase):
    def test_stack(self):
        stack = Stack()
        self.assertEqual(None, stack.peek())

        stack.push(1)
        self.assertEqual([1], stack.to_array())
        self.assertEqual(1, stack.peek())
        stack.push(2)
        self.assertEqual([2, 1], stack.to_array())
        self.assertEqual(2, stack.peek())
        stack.push(3)
        self.assertEqual([3, 2, 1], stack.to_array())
        self.assertEqual(3, stack.peek())
        stack.push(4)
        self.assertEqual([4, 3, 2, 1], stack.to_array())
        self.assertEqual(4, stack.peek())
        stack.push(5)
        self.assertEqual([5, 4, 3, 2, 1], stack.to_array())
        self.assertEqual(5, stack.peek())

        stack.pop()
        self.assertEqual([4, 3, 2, 1], stack.to_array())
        self.assertEqual(4, stack.peek())
        stack.pop()
        self.assertEqual([3, 2, 1], stack.to_array())
        self.assertEqual(3, stack.peek())
        stack.pop()
        self.assertEqual([2, 1], stack.to_array())
        self.assertEqual(2, stack.peek())
        stack.pop()
        self.assertEqual([1], stack.to_array())
        self.assertEqual(1, stack.peek())
        stack.pop()
        self.assertEqual([], stack.to_array())
        self.assertEqual(None, stack.peek())
        stack.pop()
        self.assertEqual([], stack.to_array())
        self.assertEqual(None, stack.peek())
