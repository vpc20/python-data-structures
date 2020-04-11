class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_key(self):
        return self.data

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def append(self, data):
        if self.is_empty():
            self.prepend(data)
            return

        curr = self.head
        while curr:
            if curr.get_next() is None:
                new_node = Node(data)
                curr.set_next(new_node)
                break
            curr = curr.get_next()

    def insert(self, data, pos):
        if pos == 1:
            self.prepend(data)
            return

        idx = 0
        curr = self.head
        while curr:
            idx += 1
            if idx == pos - 1:
                new_node = Node(data)
                new_node.set_next(curr.get_next())
                curr.set_next(new_node)
                break
            curr = curr.get_next()

    def update(self, old_data, new_data):
        curr = self.head
        while curr:
            if old_data == curr.get_key():
                curr.set_data(new_data)
                return True
            curr = curr.get_next()
        else:
            return False

    def delete(self, data):
        curr = self.head
        prev = self.head
        while curr:
            if data == curr.get_key():
                if curr == prev:  # first item in linked list
                    self.head = curr.get_next()
                    curr.next = None
                else:
                    prev.set_next(curr.get_next())
                return True
            prev = curr
            curr = curr.get_next()
        else:
            return False

    def search(self, data):
        curr = self.head
        while curr:
            if data == curr.get_key():
                return True
            curr = curr.get_next()
        else:
            return False

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.get_key())
            curr = curr.get_next()


list1 = LinkedList()

print('Is list empty - ', list1.is_empty())
# list1.prepend('ccc')
list1.prepend('bbb')
list1.append('ddd')
list1.append('eee')
list1.prepend('aaa')

list1.insert('ccc', 3)
list1.insert('fff', 6)
list1.insert('a11', 1)

# print list1.delete('ccc')
# list1.delete('aaa')
# list1.delete('eee')

# print list1.update('aaa', 'aa1')
# print list1.update('ccc', 'cc1')
# print list1.update('eex', 'ee1')

print('=============== Linked List ===============')
list1.print_list()
print('=============== end of list ===============')

# print list1. search('xxx')
# print list1. search('aaa')
# print list1. search('ccc')
# print list1. search('eee')
# print list1. search('bbb')
# print list1. search('ddd')

# print list1. search('aab')
# print list1. search('ccd')
# print list1. search('ddf')
