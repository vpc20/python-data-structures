class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        curr = self.head
        s = ''
        while curr:
            s += str(curr.data) + ' '
            if curr.next is not None:
                s += '==> '
            curr = curr.next
        return s

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # def append(self, data):
    #     if self.head is None:
    #         self.prepend(data)
    #     else:
    #         curr = self.head
    #         while curr:
    #             if curr.next is None:
    #                 new_node = Node(data)
    #                 curr.next = new_node
    #                 return
    #             curr = curr.next

    def append(self, val):
        if self.head is None:
            self.prepend(val)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            new_node = Node(val)
            curr.next = new_node

    # def insert(self, data, pos):
    #     if pos == 1:
    #         self.prepend(data)
    #         return
    #
    #     curr = self.head
    #     i = 1
    #     while curr:
    #         if i == pos - 1:
    #             new_node = Node(data)
    #             new_node.next = curr.next
    #             curr.next = new_node
    #         i += 1
    #         curr = curr.next

    def insert(self, data, pos):
        if pos == 1:
            self.prepend(data)
            return

        curr = self.head
        i = 1
        while curr and i != pos - 1:
            i += 1
            curr = curr.next
        if curr:
            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node

    def update(self, new_data, pos):
        curr = self.head
        i = 1
        while curr:
            if i == pos:
                curr.data = new_data
                return
            i += 1
            curr = curr.__next__

    def replace(self, old_data, new_data):
        curr = self.head
        while curr:
            if curr.data == old_data:
                curr.data = new_data
                return
            curr = curr.__next__

    def remove(self, data):
        curr = self.head
        prev = self.head
        while curr:
            if data == curr.data:
                if curr == prev:  # first item in linked list
                    self.head = curr.next
                    del curr
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def delete(self, pos):
        curr = self.head
        if pos == 1:
            self.head = curr.next
            del curr

        i = 1
        while curr:
            if i == pos - 1:
                next = curr.next
                curr.next = next.next
                next = None
                return
            i += 1
            curr = curr.next

    def peek(self, pos):
        curr = self.head
        i = 1
        while curr:
            if i == pos:
                print(curr.data)
                return
            i += 1
            curr = curr.next
        print('No data found in position', pos)

    def index(self, data):
        curr = self.head
        i = 1
        while curr:
            if data == curr.data:
                return i
            i += 1
            curr = curr.next
        return -1

    def length(self):
        curr = self.head
        i = 0
        while curr:
            i += 1
            curr = curr.next
        return i

    def to_array(self):
        curr = self.head
        arr = []
        while curr:
            arr.append(curr.data)
            curr = curr.next
        return arr

    def middle(self):
        mid = self.head
        last = self.head
        while last is not None:
            last = last.next
            if last is None:
                return mid.data
            last = last.next
            mid = mid.next
        return mid.data

    def reverse(self):
        def reverse_aux(curr, prev):
            if curr.next is None:
                self.head = curr
                curr.next = prev
                return
            next = curr.next
            curr.next = prev
            reverse_aux(next, curr)

        if self.head is None:
            return
        reverse_aux(self.head, None)


list1 = LinkedList()
list1.append(222)
list1.append(333)
list1.append(444)
list1.prepend(111)
list1.append(555)

# print list1

# list1.peek(5)
# list1.peek(10)

# print list1.index(111)
# print list1.index(3)

list1.insert('aaa', 10)
print(list1)
print(list1.length())
list1.peek(3)
print(list1)
list1.remove(222)
print(list1)
list1.delete(3)
print(list1)
print(list1.index(555))
print(list1.to_array())

list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)

print(list1)
list1.reverse()
print(list1)
