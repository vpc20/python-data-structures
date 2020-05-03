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


if __name__ == '__main__':
    bst = random_bst()
    bst.print_preorder()
    bst.print_inorder()
    bst.print_postorder()
    # print(height(bst.root))
    # print(height_dfs(bst.root))

    # bst1 = BinarySearchTree()
    # bst1.insert(77)
    # bst1.insert(3)
    # bst1.insert(42)
    # bst1.insert(14)
    # bst1.insert(4)
    # bst1.insert(71)
    # bst1.insert(51)
    # bst1.insert(43)
    # bst1.insert(59)
    # print('--------------------------------------')
    # print(height(bst1.root))
    # print(height_dfs(bst1.root))

    # 77, 3, 42, 14, 4, 71, 51, 43, 59

    # for _ in range(100):
    #     bst = random_bst()
    #     bst.print_inorder()
    #     assert is_valid_bst(bst) == True
    #
    # node1 = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # bst = BinarySearchTree()
    # bst.root = node2
    # node2.right = node1
    # print(is_valid_bst(bst))
