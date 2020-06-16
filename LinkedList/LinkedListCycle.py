# Given a linked list, determine if it has a cycle in it.
# To represent a cycle in the given linked list, we use an integer pos which represents the
# position(0 - indexed) in the linked list where tail connects to.If pos is -1, then there is no cycle in the linked
# list.
#
# Example 1:
# Input: head = [3, 2, 0, -4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
from LinkedList.LinkedListx import linked_list


# def has_cycle(curr):
#     nset = set()
#     while curr:
#         if curr in nset:
#             return True
#         nset.add(curr)
#         curr = curr.next
#     return False


def has_cycle(curr):
    if curr is None or curr.next is None:
        return False

    slow = curr
    fast = curr.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


list1 = linked_list([1, 2, 3, 4, 5, 6, 7])
print(list1)
print(has_cycle(list1))

list1 = linked_list([1, 2, 3, 4, 5, 6, 7])
list1.next.next.next.next = list1
print(has_cycle(list1))
