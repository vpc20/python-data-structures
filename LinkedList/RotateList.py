# Given a linked list, rotate the list to the right by k places, where k is non-negative.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
#
# Example 2:
#
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULLMiddleOfLinkedList.pyMiddleOfLinkedList.py
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
from LinkedList.LinkedListx import linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(curr):
    while curr:
        print(curr.val, end=' ')
        curr = curr.next
    print('')


def rotate_right(head, k):
    if head is None:
        return None
    if k == 0:
        return head

    l = length_list(head)
    return rotate_left(head, l - k % l)


def rotate_left(head, k):
    if head is None:
        return None
    k = k % length_list(head)
    if k == 0:
        return head

    curr = head
    i = 1
    while curr.next:
        if i == k:
            new_tail = curr
            new_head = curr.next
        i += 1
        curr = curr.next
    tail = curr
    tail.next = head
    new_tail.next = None
    return new_head


def length_list(head):
    curr = head
    l = 0
    while curr:
        l += 1
        curr = curr.next
    return l


list1 = linked_list([1, 2, 3, 4, 5])
print(list1)
print(rotate_left(list1, 1))

list1 = linked_list([1, 2, 3, 4, 5])
print(list1)
print(rotate_right(list1, 1))
