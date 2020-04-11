import unittest
from random import randrange
from heapq import heapify, heappush, heappop


def is_min_heap(arr):
    for i in range(1, len(arr)):
        if arr[((i - 1) / 2)] > arr[i]:  # parent > child
            return False
    return True


def min_maintain_heap(arr, i):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < len(arr) and arr[l] <= arr[i]:
        smallest = l
    else:
        smallest = i
    if r < len(arr) and arr[r] <= arr[smallest]:
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_maintain_heap(arr, smallest)


def min_heapify(arr):
    for i in range((len(arr) - 1) // 2, -1, -1):
        min_maintain_heap(arr, i)


def min_bubble_up(arr, i):
    pi = int((i - 1) / 2)  # parent index
    while i > 0 and arr[pi] > arr[i]:
        arr[i], arr[pi] = arr[pi], arr[i]
        i = pi
        pi = int((i - 1) / 2)


def min_heap_push(arr, key):
    arr.append(key)
    min_bubble_up(arr, len(arr) - 1)


def min_heap_pop(arr):
    minkey = arr[0]
    last = arr.pop()
    if arr:
        arr[0] = last
        min_maintain_heap(arr, 0)
    return minkey


def random_int_array(max_size, max_int):
    return [randrange(max_int + 1) for _ in range(randrange(max_size + 1))]


if __name__ == '__main__':
    # list1 = [1, 3, 5, 2, 4, 6]
    # min_heapify(list1)
    # print(list1)

    lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    lst1 = lst.copy()
    print('list            ', lst)

    heapify(lst)
    print('heapify list    ', lst)
    min_heapify(lst1)
    print('min_heapify list', lst1)

    print('-' * 64)

    lst = [3, 6, 9]
    heappush(lst, 2)
    print(lst)
    print(heappop(lst))
    print(lst)

    print('-' * 64)

    lst1 = [3, 6, 9]
    min_heap_push(lst1, 2)
    print(lst1)
    print(min_heap_pop(lst1))
    print(lst1)

    # heapq.heappop(lst)
    # print lst
    # heapq.heappush(lst,1)
    # print lst
    # heapq.heappushpop(lst,10)
    # print lst
    # heapq.heapreplace(lst,15) # pop then push
    # print lst

    # a = [2, 1, 3]
    # a = [9, 6, 7, 3]
    # a = [9, 6, 7, 3, 2]
    # min_bubble_up(a, 4)
    # print(a)
