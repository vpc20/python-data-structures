# Given the head of a linked list and a value x, partition it such that all nodes less than x
# come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# Example 1:
# Input: head = [1, 4, 3, 2, 5, 2], x = 3
# Output: [1, 2, 2, 4, 3, 5]
#
# Example 2:
# Input: head = [2, 1], x = 2
# Output: [1, 2]
#
# Constraints:
# The number of nodes in the list is in the range[0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
from LinkedList.LinkedListx import linked_list, ListNode


def partition(head, x):
    curr = head
    head1 = head2 = curr1 = curr2 = None

    while curr:
        if curr.val < x:
            if head1 is None:
                head1 = ListNode(curr.val)
                curr1 = head1
            else:
                curr1.next = ListNode(curr.val)
                curr1 = curr1.next
        else:
            if head2 is None:
                head2 = ListNode(curr.val)
                curr2 = head2
            else:
                curr2.next = ListNode(curr.val)
                curr2 = curr2.next
        curr = curr.next

    if curr1:
        curr1.next = head2
        return head1
    else:
        return head2


# def partition(head, x):
#     curr = head
#     less = less_head = ListNode(0)
#     more = more_head = ListNode(0)
#
#     while curr:
#         if curr.val < x:
#             less.next = curr
#             less = less.next
#         else:
#             more.next = curr
#             more = more.next
#         curr = curr.next
#
#     more.next = None
#     less.next = more_head.next
#     return less_head.next


# def partition(head, x):
#     if not head:
#         return None
#     curr = head
#     prev = None
#     lastless = head
#
#     while curr:
#         if curr.val < x:
#             if lastless == head == curr:
#                 pass
#             else:
#                 prev.next = curr.next
#                 curr.next = lastless.next
#                 lastless.next = curr
#                 lastless = lastless.next
#                 curr = prev.next
#                 continue
#         prev = curr
#         curr = curr.next
#
#     return head


# list1 = linked_list([1, 4, 3, 2, 5, 2])
# print(list1)
# print(partition(list1, 3))

# list1 = linked_list([2, 1])
# print(list1)
# print(partition(list1, 2))

# list1 = linked_list([1, 1])
# print(list1)
# print(partition(list1, 0))

list1 = linked_list([5, 4, 3, 2, 1])
print(list1)
print(partition(list1, 3))

list1 = linked_list([5])
print(list1)
print(partition(list1, 3))

list1 = linked_list([])
print(list1)
print(partition(list1, 3))
