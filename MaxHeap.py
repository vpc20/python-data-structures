import unittest
from random import randrange


class MaxHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def is_max_heap(self):
        for child_idx in range(1, self.size()):
            parent_idx = (child_idx - 1) / 2
            if self.heap[child_idx] > self.heap[parent_idx]:
                return False
        return True

    def find_max(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def insert(self, key):
        self.heap.append(key)
        if self.size() > 1:
            self.sift_up()

    def extract_max(self):
        if self.size() == 0:
            return None
        else:
            max_key = self.heap[0]
            self.heap[0] = self.heap[-1]  # put last item on top of the heap
            self.heap.pop()  # remove last item
            self.sift_down(0, self.size() - 1)
            return max_key

    def sift_up(self):
        curr_idx = self.size() - 1
        parent_idx = (curr_idx - 1) / 2

        while self.heap[curr_idx] > self.heap[parent_idx] and parent_idx >= 0:
            self.heap[curr_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[curr_idx]
            curr_idx = parent_idx
            parent_idx = (curr_idx - 1) / 2

    def sift_down(self, curr_idx, last_idx):
        # larger_idx = 0
        while True:
            left_idx = 2 * curr_idx + 1
            if left_idx >= last_idx:
                break  # no children
            right_idx = 2 * curr_idx + 2
            if right_idx >= last_idx:
                larger_idx = left_idx
            elif self.heap[left_idx] > self.heap[right_idx]:
                larger_idx = left_idx
            else:
                larger_idx = right_idx

            if self.heap[curr_idx] < self.heap[larger_idx]:
                self.heap[curr_idx], self.heap[larger_idx] = self.heap[larger_idx], self.heap[curr_idx]
                curr_idx = larger_idx
            else:
                break

    def max_heapify(self):
        for i in range(self.size() // 2, -1, -1):
            self.sift_down(i, self.size() - 1)

    def create_max_heap(self, lst):
        self.heap = []
        for item in lst:
            self.insert(item)

    def heap_sort(self):
        sorted_list = [0] * self.size()
        for i in range(self.size() - 1, -1, -1):
            sorted_list[i] = self.extract_max()
        return sorted_list


def random_int_array(max_size, max_int):
    return [randrange(max_int + 1) for _ in range(randrange(max_size + 1))]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

        max_heap = MaxHeap()

        for i in range(10000):
            a1 = random_int_array(20, 100)
            max_heap.create_max_heap(a1)
            print(a1)
            self.assertEqual(max_heap.is_max_heap(), True)

            # for i in range(10000):
            #     a1 = random_int_array(20, 100)
            #     a2 = list(a1)
            #     print a1
            #     heapsort(a1)
            #     self.assertEqual(a1, sorted(a2))


if __name__ == '__main__':
    unittest.main()

# max_heap = MaxHeap()

# print max_heap.size()
# print max_heap.is_empty()
# print max_heap.find_max()
#
# max_heap.insert(1)
# max_heap.insert(2)
# max_heap.insert(3)
# max_heap.insert(4)
# max_heap.insert(5)
# print max_heap
#
# print max_heap.extract_max()
# print max_heap
# print max_heap.extract_max()
# print max_heap
# print max_heap.extract_max()
# print max_heap
# print max_heap.extract_max()
# print max_heap
# print max_heap.extract_max()
# print max_heap
# print max_heap.extract_max()
# print max_heap

# max_heap.create_max_heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print max_heap
# print max_heap.is_max_heap()
#
# max_heap.max_heapify()
# print max_heap
# print max_heap.is_max_heap()
