# Given the head of a linked list and an integer val, remove all the nodes of the linked list
# that has Node.val == val, and return the new head.
#
# Example 1:
# Input: head = [1, 2, 6, 3, 4, 5, 6], val = 6
# Output: [1, 2, 3, 4, 5]
#
# Example 2:
# Input: head = [], val = 1
# Output: []
#
# Example 3:
# Input: head = [7, 7, 7, 7], val = 7
# Output: []
#
# Constraints:
# The number of nodes in the list is in the range[0, 104].
# 1 <= Node.val <= 50
# 0 <= k <= 50

from LinkedList.LinkedListx import linked_list


def remove_elements(head, val):
    while head is not None and head.val == val:
        head = head.next

    if head is None:
        return None
    prev = head
    curr = head.next

    while curr is not None:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return head

# creates a new list
# def remove_elements(head, val):
#     if head is None:
#         return None
#     head2 = curr2 = None
#
#     while head is not None:
#         if head.val != val:
#             if curr2 is None:
#                 head2 = ListNode(head.val)
#                 curr2 = head2
#             else:
#                 curr2.next = ListNode(head.val)
#                 curr2 = curr2.next
#         head = head.next
#
#     return head2


# class Solution:
#     def removeElements(self, head, val):
#         """
#         :type head: ListNode
#         :type val: int
#         :rtype: ListNode
#         """
#
#         dummy_head = ListNode(-1)
#         dummy_head.next = head
#
#         current_node = dummy_head
#         while current_node.next != None:
#             if current_node.next.val == val:
#                 current_node.next = current_node.next.next
#             else:
#                 current_node = current_node.next
#
#         return dummy_head.next


# list1 = linked_list([6, 6, 6, 6, 6, 1, 2, 6, 3, 4, 5, 6])

list1 = linked_list([1, 2, 6, 3, 4, 5, 6])
print(list1)
print(remove_elements(list1, 6))

list1 = linked_list([1, 2, 2, 1])
print(list1)
print(remove_elements(list1, 2))
