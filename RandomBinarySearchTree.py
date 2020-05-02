import random


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, new_val):
        if self.root is None:  # empty tree
            self.root = Node(new_val)
            return

        new_node = Node(new_val)
        curr = self.root
        while True:
            if new_val < curr.val:
                if curr.left is None:
                    curr.left = new_node
                    return
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = new_node
                    return
                else:
                    curr = curr.right

    def print_preorder(self):
        def preorder_aux(curr):
            print(curr.val, end=' ')
            if curr.left:
                preorder_aux(curr.left)
            if curr.right:
                preorder_aux(curr.right)

        preorder_aux(self.root)
        print('')

    def print_inorder(self):
        def inorder_aux(curr):
            if curr.left:
                inorder_aux(curr.left)
            print(curr.val, end=' ')
            if curr.right:
                inorder_aux(curr.right)

        inorder_aux(self.root)
        print('')

    def print_postorder(self):
        def postorder_aux(curr):
            if curr.left:
                postorder_aux(curr.left)
            if curr.right:
                postorder_aux(curr.right)
            print(curr.val, end=' ')

        postorder_aux(self.root)
        print('')


def random_bst(num_nodes=50, max_intval=1000):
    seen = set()
    bst = BinarySearchTree()
    for i in range(num_nodes):
        r = random.randint(1, max_intval)
        if r not in seen:
            bst.insert(r)
            seen.add(r)
    return bst


bst = random_bst(10, 100)
bst.print_preorder()
bst.print_inorder()
bst.print_postorder()
