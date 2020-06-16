from LinkedList.LinkedListx import linked_list


# def reverse_list(head):
#     def revlist(prev, curr):
#         if curr is None:
#             return prev
#         nxt = curr.next
#         curr.next = prev
#         return revlist(curr, nxt)
#     return revlist(None, head)

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# def reverse_list(head):
#     prev = None
#     curr = head
#     while curr:
#         curr.next, prev, curr = prev, curr, curr.next
#     return prev

list1 = linked_list([1, 2, 3, 4, 5, 6, 7])
print(list1)
print(reverse_list(list1))
