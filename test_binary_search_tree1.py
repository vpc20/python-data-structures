from unittest import TestCase
from itertools import permutations

from BinarySearchTree1 import BinarySearchTree


class TestBinarySearchTree(TestCase):
    def test_preorder(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        for r in range(1, len(arr) + 1):
            for perm in permutations(arr, r):
                bst = BinarySearchTree()
                for e in perm:
                    bst.insert(e)
                print(perm)
                print(bst.preorder_arr())
                self.assertEqual(bst.preorder_arr(), bst.preorder_iter_arr())
                del bst

    def test_inorder(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        for r in range(1, len(arr) + 1):
            for perm in permutations(arr, r):
                bst = BinarySearchTree()
                for e in perm:
                    bst.insert(e)
                print(perm)
                print(bst.inorder_arr())
                self.assertEqual(bst.inorder_arr(), bst.inorder_iter_arr())
                del bst

    def test_postorder(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        for r in range(1, len(arr) + 1):
            for perm in permutations(arr, r):
                bst = BinarySearchTree()
                for e in perm:
                    bst.insert(e)
                print(perm)
                print(bst.postorder_arr())
                self.assertEqual(bst.postorder_arr(), bst.postorder_iter_arr())
                del bst

    # def test_insert(self):
    #     bst = BinarySearchTree()
    #     bst.insert(4)
    #     self.assertEqual([4], bst.to_array())
    #     bst.insert(2)
    #     self.assertEqual([2, 4], bst.to_array())
    #     bst.insert(6)
    #     self.assertEqual([2, 4, 6], bst.to_array())
    #     bst.insert(1)
    #     self.assertEqual([1, 2, 4, 6], bst.to_array())
    #     bst.insert(3)
    #     self.assertEqual([1, 2, 3, 4, 6], bst.to_array())
    #     bst.insert(5)
    #     self.assertEqual([1, 2, 3, 4, 5, 6], bst.to_array())
    #     bst.insert(7)
    #     self.assertEqual([1, 2, 3, 4, 5, 6, 7], bst.to_array())
    #
    # self.assertEqual(1, bst.find_min())
    # self.assertEqual(7, bst.find_max())
    #
    # self.assertEqual(1, bst.search(1))
    # self.assertEqual(2, bst.search(2))
    # self.assertEqual(3, bst.search(3))
    # self.assertEqual(4, bst.search(4))
    # self.assertEqual(5, bst.search(5))
    # self.assertEqual(6, bst.search(6))
    # self.assertEqual(7, bst.search(7))
    # self.assertEqual(None, bst.search(0))
    # self.assertEqual(None, bst.search(8))
    #
    # self.assertEqual(None, bst.height(0))
    # self.assertEqual(2, bst.height(4))
    # self.assertEqual(1, bst.height(2))
    # self.assertEqual(1, bst.height(6))
    # self.assertEqual(0, bst.height(1))
    # self.assertEqual(0, bst.height(3))
    # self.assertEqual(0, bst.height(5))
    # self.assertEqual(0, bst.height(7))
    #
    # self.assertEqual(0, bst.depth(4))
    # self.assertEqual(1, bst.depth(2))
    # self.assertEqual(1, bst.depth(6))
    # self.assertEqual(2, bst.depth(1))
    # self.assertEqual(2, bst.depth(3))
    # self.assertEqual(2, bst.depth(5))
    # self.assertEqual(2, bst.depth(7))
    # self.assertEqual(None, bst.depth(8))
    #
    # self.assertEqual(None, bst.successor(0))
    # self.assertEqual(2, bst.successor(1))
    # self.assertEqual(3, bst.successor(2))
    # self.assertEqual(4, bst.successor(3))
    # self.assertEqual(5, bst.successor(4))
    # self.assertEqual(6, bst.successor(5))
    # self.assertEqual(7, bst.successor(6))
    # self.assertEqual(None, bst.successor(7))
    #
    # self.assertEqual(None, bst.predecessor(0))
    # self.assertEqual(None, bst.predecessor(1))
    # self.assertEqual(1, bst.predecessor(2))
    # self.assertEqual(2, bst.predecessor(3))
    # self.assertEqual(3, bst.predecessor(4))
    # self.assertEqual(4, bst.predecessor(5))
    # self.assertEqual(5, bst.predecessor(6))
    # self.assertEqual(6, bst.predecessor(7))
    # self.assertEqual(None, bst.predecessor(8))
