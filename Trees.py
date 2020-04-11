from collections import deque


class Node:
    def __init__(self, key):  # left-child, right-sibling representation
        self.key = key
        self.parent = None
        self.left_child = None
        self.right_sibling = None


class Tree:
    def __init__(self):
        self.root = None

    def traversal(self):
        queue = deque([self.root])
        print(self.root.key)
        print(f'self.root.parent: {self.root.parent}')
        if self.root.left_child:
            print(f'self.root.left_child: {self.root.left_child.key}')
        else:
            print(f'self.root.left_child: {self.root.left_child}')
        if self.root.right_sibling:
            print(f'self.root.right_sibling: {self.root.right_sibling.key}')
        else:
            print(f'self.root.right_sibling: {self.root.right_sibling}')
        while queue:
            curr = queue.popleft()
            if curr.left_child:
                curr_child = curr.left_child
                while curr_child:
                    queue.append(curr_child)
                    print(curr_child.key)
                    print(f'parent: {curr_child.parent.key}')
                    if curr_child.left_child:
                        print(f'left_child: {curr_child.left_child.key}')
                    else:
                        print(f'left_child: {curr_child.left_child}')
                    if curr_child.right_sibling:
                        print(f'right_sibling: {curr_child.right_sibling.key}')
                    else:
                        print(f'right_sibling: {curr_child.right_sibling}')
                    curr_child = curr_child.right_sibling

    # def search(self, pkey):
    #     pnode = None
    #     last_child = None
    #
    #     queue = deque([self.root])
    #     while queue:
    #         curr = queue.popleft()
    #         if curr.key == pkey:
    #             pnode = curr
    #         if curr.left_child:
    #             curr_child = curr.left_child
    #             while curr_child:
    #                 queue.append(curr_child)
    #                 last_child = curr_child
    #                 curr_child = curr_child.right_sibling
    #             if pnode:
    #                 break
    #         else:
    #             if pnode:
    #                 last_child = None
    #                 break
    #     return pnode, last_child

    def search(self, skey):
        keynode = None
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            if curr.key == skey:
                keynode = curr
                break
            if curr.left_child:
                curr_child = curr.left_child
                while curr_child:
                    queue.append(curr_child)
                    curr_child = curr_child.right_sibling
        return keynode

    @staticmethod
    def last_child(pnode):
        last_child_node = None
        if pnode.left_child:
            curr_child = pnode.left_child
            while curr_child:
                last_child_node = curr_child
                curr_child = curr_child.right_sibling
        return last_child_node

    def insert(self, new_key, pkey):
        if self.root is None:
            self.root = Node(new_key)
        else:
            new_node = Node(new_key)
            pnode = self.search(pkey)  # look for parent
            if pnode:
                new_node.parent = pnode
                if pnode.left_child is None:
                    pnode.left_child = new_node  # new node is the first child
                else:
                    last_child_node = self.last_child(pnode)
                    last_child_node.right_sibling = new_node  # new node is last child
            else:
                raise KeyError(f'Parent key error: {pkey}')


if __name__ == '__main__':
    t = Tree()
    t.insert(1, '')
    t.insert(2, 1)
    t.insert(3, 1)
    t.insert(4, 1)
    t.insert(5, 2)
    t.insert(6, 2)
    # t.insert(7, 9)  # error testing
    t.traversal()

    # node1 = Node(1)
    # t.root = node1
    #
    # node4 = Node(4)
    # node4.parent = node1
    # node4.left_child = None
    # node4.right_sibling = None
    #
    # node3 = Node(3)
    # node3.parent = node1
    # node3.left_child = None
    # node3.right_sibling = node4
    #
    # node2 = Node(2)
    # node2.parent = node1
    # node2.left_child = None
    # node2.right_sibling = node3
    #
    # node5 = Node(5)
    # node5.parent = node2
    # node5.left_child = None
    # node5.right_sibling = None
    # node2.left_child = node5
    #
    # node1.parent = None
    # node1.left_child = node2
    # node1.right_sibling = None
    #
    # t.traversal()

# 1
# self.root.parent: None
# self.root.left_child: 2
# self.root.right_sibling: None
# 2
# parent: 1
# left_child: 5
# right_sibling: 3
# 3
# parent: 1
# left_child: None
# right_sibling: 4
# 4
# parent: 1
# left_child: None
# right_sibling: None
# 5
# parent: 2
# left_child: None
# right_sibling: 6
# 6
# parent: 2
# left_child: None
# right_sibling: None
