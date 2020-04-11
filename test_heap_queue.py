import random
from heapq import heapify, heappush, heappop
from unittest import TestCase

from HeapQueue import min_heapify, min_heap_push, min_heap_pop
from random_data import random_int_array


class TestHeapQueue(TestCase):
    def test_min_heapify(self):
        for i in range(1000):
            a1 = random_int_array(20, 100)
            print(a1)
            a2 = a1.copy()
            heapify(a1)
            print(a1)
            min_heapify(a2)
            print(a2)
            self.assertEqual(a1, a2)

    def test_min_heap_push(self):
        for i in range(1000):
            r = random.randrange(100)
            print(r)

            a1 = random_int_array(20, 100)
            a2 = a1.copy()

            heappush(a1, r)
            print(a1)
            min_heap_push(a2, r)
            print(a2)

            self.assertEqual(a1, a2)

    def test_min_heap_pop(self):
        for i in range(1000):
            a1 = random_int_array(20, 100)
            if not a1:
                continue
            heapify(a1)
            a2 = a1.copy()
            print('test array', a1)

            minkey1 = heappop(a1)
            print(minkey1, a1)
            minkey2 = min_heap_pop(a2)
            print(minkey2, a2)

            self.assertEqual(minkey1, minkey2)
            self.assertEqual(a1, a2)
