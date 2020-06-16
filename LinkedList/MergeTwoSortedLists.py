# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the
# nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
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


# def merge_two_lists(l1, l2):
#     if l1 is None:
#         return l2
#     if l2 is None:
#         return l1
#
#     if l1.val <= l2.val:
#         l1.next = merge_two_lists(l1.next, l2)
#         return l1
#     else:
#         l2.next = merge_two_lists(l1, l2.next)
#         return l2

# def merge_two_lists(l1, l2):
#     if l1 is None:
#         if l2 is None:
#             return None
#         else:
#             return l2
#     else:
#         if l2 is None:
#             return l1
#
#     curr1 = l1
#     curr2 = l2
#     if curr1.val < curr2.val:
#         head = curr3 = curr1
#         curr1 = curr1.next
#     else:
#         head = curr3 = curr2
#         curr2 = curr2.next
#
#     while curr1 and curr2:
#         if curr1.val < curr2.val:
#             curr3.next = curr1
#             curr1 = curr1.next
#         else:
#             curr3.next = curr2
#             curr2 = curr2.next
#         curr3 = curr3.next
#
#     if curr1:
#         curr3.next = curr1
#
#     if curr2:
#         curr3.next = curr2
#
#     return head


def merge_two_lists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    curr1 = l1
    curr2 = l2

    if curr1.val < curr2.val:
        head = curr3 = curr1
        curr1 = curr1.next
    else:
        head = curr3 = curr2
        curr2 = curr2.next

    while curr1 and curr2:
        if curr1.val < curr2.val:
            curr3.next = curr1
            curr1 = curr1.next
        else:
            curr3.next = curr2
            curr2 = curr2.next
        curr3 = curr3.next

    if curr1:
        curr3.next = curr1

    if curr2:
        curr3.next = curr2

    return head


# def merge_two_lists(l1, l2):
#     if l1 is None:
#         if l2 is None:
#             return None
#         else:
#             return l2
#     else:
#         if l2 is None:
#             return l1
#
#     curr1 = l1
#     curr2 = l2
#     if curr1.val < curr2.val:
#         head = curr1
#     else:
#         head = curr2
#
#     while curr1 and curr2:
#         next1 = curr1.next
#         next2 = curr2.next
#         if curr1.val < curr2.val:
#             curr1.next = curr2
#         else:
#             curr2.next = curr1
#
#         if next1 is None:
#             tail1 = curr1
#         if next2 is None:
#             tail2 = curr2
#
#         curr1 = next1
#         curr2 = next2
#
#     if curr1:
#         tail2.next = curr1
#
#     if curr2:
#         tail1.next = curr2
#
#     return head


list1 = linked_list([3, 5])
list2 = linked_list([1, 2, 4])
print_list(merge_two_lists(list1, list2))
