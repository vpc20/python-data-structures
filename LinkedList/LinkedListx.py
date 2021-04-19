class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ''
        curr = self
        while curr:
            s += str(curr.val) + ' --> '
            curr = curr.next
        return s[:-5]

    def __repr__(self):
        return f'ListNode({self.val})'


def linked_list(vals):
    if not vals:
        return None

    head = curr = ListNode(vals[0])
    for val in vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


if __name__ == '__main__':
    list1 = linked_list([])
    print(list1)
    list1 = linked_list([1])
    print(list1)
    list1 = linked_list([1, 2])
    print(list1)
    list1 = linked_list([1, 2, 3])
    print(list1)
