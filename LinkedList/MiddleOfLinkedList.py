# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
#
# If there are two middle nodes, return the second middle node.
#
# Example 1:
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
#
# Example 2:
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.
#
# Note:
# The number of nodes in the given list will be between 1 and 100.


# def middle_node(head):
#     curr = head
#     arr = []
#     while curr:
#         arr.append(curr)
#         curr = curr.next
#     return arr[int(len(arr) / 2)]

# def middle_node(self, head: ListNode) -> ListNode:
#     mid = head
#     last = head
#     while last is not None:
#         last = last.next
#         if last is None:
#             return mid
#         last = last.next
#         mid = mid.next
#     return mid
from LinkedList.LinkedListx import ListNode


def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# def middleNode(self, head):
#     A = [head]
#     while A[-1].next:
#         A.append(A[-1].next)
#     return A[len(A) / 2]


node1 = ListNode(1)
head = node1
assert middle_node(head) == node1

node2 = ListNode(2)
node1.next = node2
assert middle_node(head) == node2

node3 = ListNode(3)
node2.next = node3
assert middle_node(head) == node2
