# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
#
# Example 2:
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
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


def is_palindrome(head):
    nodes = []

    curr = head
    while curr:
        nodes.append(curr.val)
        curr = curr.next

    curr = head
    while curr:
        if curr.val != nodes.pop():
            return False
        curr = curr.next

    return True


list1=linked_list([1, 2, 3, 2, 1])
print_list(list1)
print(is_palindrome(list1))
