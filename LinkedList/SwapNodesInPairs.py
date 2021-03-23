# Given a linked list, swap every two adjacent nodes and return its head.
#
# Example 1:
# Input: head = [1, 2, 3, 4]
# Output: [2, 1, 4, 3]
#
# Example 2:
# Input: head = []
# Output: []
#
# Example 3:
# Input: head = [1]
# Output: [1]
#
# Constraints:
# The number of nodes in the list is in the range[0, 100].
# 0 <= Node.val <= 100
#
# Follow up: Can you solve the problem without modifying the values in the list's nodes?
#  (i.e., Only nodes themselves may be changed.)

from LinkedList.LinkedListx import linked_list


def swap_pairs(head):
    if head is None:
        return None
    if head.next is None:
        return head
    curr = head
    while True:
        curr.val, curr.next.val = curr.next.val, curr.val
        if curr.next.next is None or curr.next.next.next is None:
            break
        curr = curr.next.next
    return head


list1 = linked_list([1])
print(list1)
print(swap_pairs(list1))

list1 = linked_list([1, 2])
print(list1)
print(swap_pairs(list1))

list1 = linked_list([1, 2, 3])
print(list1)
print(swap_pairs(list1))

list1 = linked_list([1, 2, 3, 4])
print(list1)
print(swap_pairs(list1))
