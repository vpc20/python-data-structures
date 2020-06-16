# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are
# talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
# Example 1:
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
#
# Example 2:
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
#
# Note:
#     The relative order inside both the even and odd groups should remain as it was in the input.
#     The first node is considered odd, the second node even and so on ...
#
# 1 2 3
# 1 3 2          move 2 to 1
#
# 1 2 3 4 5
# 1 3 2 4 5      move 2 to 1
# 1 3 5 2 4      move 4 to 2
#
# 1 2 3 4 5 6 7
# 1 3 2 4 5 6 7  move 2 to 1
# 1 3 5 2 4 6 7  move 4 to 2
# 1 3 5 7 2 4 6  move 6 to 3
#
# 1 2 3 4 5 6 7 8 9
# 1 3 2 4 5 6 7 8 9  move 2 to 1
# 1 3 5 2 4 6 7 8 9  move 4 to 2
# 1 3 5 7 2 4 6 8 9  move 6 to 3
# 1 3 5 7 9 2 4 6 8  move 8 to 4


# 1 2 3
# 1 3 2          move 2 to 1

# 1 2 3 4 5
# 1 3 2 4 5      move 2 to 1
# 1 3 5 2 4      move 4 to 2

# def odd_even_list(head):
#     curr = head
#     if curr is None or curr.next is None or curr.next.next is None:
#         return head
#
#     i = 2
#     prev_odd = curr
#     prev_node = curr.next
#     even_head = curr.next  # does not change
#     curr = curr.next.next
#     while curr:
#         if i % 2 == 0:  # odd node because i starts from zero
#             prev_odd.next = curr
#             prev_node.next = curr.next
#             curr.next = even_head
#             prev_odd = curr
#             curr = prev_node
#         else:
#             prev_node = curr
#         curr = curr.next
#         i += 1
#     return head
from LinkedList.LinkedListx import linked_list


def odd_even_list(head):
    if head is None or head.next is None or head.next.next is None:
        return head

    odd = head
    even = odd.next
    even_head = even
    curr = even.next
    is_odd = True
    while curr:
        if is_odd:
            odd.next = curr
            odd = curr
            is_odd = False
        else:
            even.next = curr
            even = curr
            is_odd = True
        curr = curr.next

    odd.next = even_head
    even.next = None
    return head


# def odd_even_list(head):
#     curr = head
#     if curr is None or curr.next is None or curr.next.next is None:
#         return head
#
#     prev_odd = curr
#     prev = curr.next
#     even_head = curr.next  # does not change
#     curr = curr.next.next
#     exit_loop = False
#     while True:
#         if curr.next:
#             prevsave = curr.next
#             if curr.next.next:
#                 currsave = curr.next.next
#             else:
#                 exit_loop = True
#         else:
#             exit_loop = True
#
#         currx = curr
#         prev_odd.next = curr
#         prev.next = curr.next
#         curr.next = even_head
#         prev_odd = currx
#
#         if exit_loop:
#             break
#         prev = prevsave
#         curr = currsave
#     return head

# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         cur = head
#         values = []
#         while cur:
#             values.append(cur.val)
#             cur = cur.next
#
#         i = 0
#         cur = head
#         while i < len(values):
#             cur.val = values[i]
#             cur = cur.next
#             i += 2
#         i = 1
#         while i < len(values):
#             cur.val = values[i]
#             cur = cur.next
#             i += 2
#         return head


# 1 2 3 4 5
# 1 3 2 4 5      move 2 to 1
# 1 3 5 2 4      move 4 to 2


list1 = linked_list([1, 2, 3, 4, 5, 6, 7])
print(list1)
print(odd_even_list(list1))
