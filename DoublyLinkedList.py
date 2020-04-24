class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head  # old head
        new_node.prev = None

        if self.head is not None:  # old head
            self.head.prev = new_node

        self.head = new_node  # new node will always be the head
        if self.tail is None:  # if doubly linked list is empty
            self.tail = new_node  # new node will be both head and tail

    def append(self, val):
        if self.head is None:  # empty list
            self.prepend(val)
        else:
            new_node = Node(val)
            new_node.next = None
            new_node.prev = self.tail  # old tail
            self.tail.next = new_node  # old tail
            self.tail = new_node  # new node will always be the tail

    def delete(self, node):
        if self.head is None:  # empty list
            return
        if node == self.head:  # node.next will be the new head
            self.head = node.next
            self.head.prev = None
        elif node == self.tail:  # node.prev will be the new tail
            self.tail = node.prev
            self.tail.next = None
        else:  # prev node and next node will be linked to each other
            node.prev.next = node.next
            node.next.prev = node.prev
        del node

    def display_forward(self):
        curr = self.head
        while curr:
            print(curr.val, end=' ')
            curr = curr.next
        print('')

    def display_reversed(self):
        curr = self.tail
        while curr:
            print(curr.val, end=' ')
            curr = curr.prev
        print('')


dl = DoublyLinkedList()
dl.prepend(3)
dl.prepend(2)
dl.prepend(1)
dl.append(4)
dl.append(5)
dl.display_forward()
dl.display_reversed()

dl.delete(dl.head)
dl.display_forward()
dl.display_reversed()

dl.delete(dl.tail)
dl.display_forward()
dl.display_reversed()

dl.delete(dl.head.next)
dl.display_forward()
dl.display_reversed()
