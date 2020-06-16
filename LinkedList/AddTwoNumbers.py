# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
from LinkedList.LinkedListx import linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=' ')
        curr = curr.next


def get_list_value(head):
    list_val = 0
    i = 0

    curr = head
    while curr:
        list_val += curr.val * 10 ** i
        i += 1
        curr = curr.next
    return list_val


def add_two_numbers(l1, l2):
    sumx = get_list_value(l1) + get_list_value(l2)
    node_vals = [int(d) for d in reversed(str(sumx))]
    head = prev = ListNode(node_vals[0])
    for val in node_vals[1:]:
        prev.next = ListNode(val)
        prev = prev.next
    return head


list1 = linked_list([2, 4, 3])
list2 = linked_list([5, 6, 4])
print_list(add_two_numbers(list1, list2))
