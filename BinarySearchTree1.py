from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

    def is_a_leaf(self):
        """
        Check if node is a leaf.
        A node with no children is a leaf or external node.
        A nonleaf node is an internal node.
        :return: True - node is a leaf (external node)
                 False - node is not a leaf (internal node)
        """
        return self.left is None and self.right is None

    def is_a_left_child(self):
        return self.parent.left.key == self.key if self.parent is not None else False

    def is_a_right_child(self):
        return self.parent.right.key == self.key if self.parent is not None else False

    def has_no_left_child(self):
        return self.left is None

    def has_no_right_child(self):
        return self.right is None

    def has_one_child(self):
        return (self.left is None and self.right is not None) or (self.left is not None and self.right is None)

    def degree(self):
        """
        The number of children of a node x in a rooted tree T equals the degree of x

        :return: degree of the node
        """
        degree = 0
        if self.left is not None:
            degree += 1
        if self.right is not None:
            degree += 1
        return degree


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        data_list = []
        self._inorder_str(self.root, data_list)
        return 'Binary Search Tree - <inorder> ' + ''.join(str(e) for e in data_list)

    def _inorder_str(self, curr, data_list):
        if curr:
            if curr.left:
                self._inorder_str(curr.left, data_list)
            data_list.append(str(curr.key) + ' ')
            if curr.right:
                self._inorder_str(curr.right, data_list)

    def is_empty(self):
        return self.root is None

    def is_valid_bst(self):
        """
        The keys in a binary search tree are always stored in such a way as to satisfy the
        binary-search-tree property:

        Let x be a node in a binary search tree. If y is a node in the left subtree of x,
        then y.key <= x.key. If y is a node in the right subtree of x, then y.key >= x.key.

        :return: True  : valid binary search tree
                 False : not a binary search tree
        """
        stack = [self.root]
        while stack:
            curr = stack.pop()
            if (curr.left is not None and curr.left.key > curr.key) \
                    or (curr.right is not None and curr.right.key < curr.key):
                return False
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return True

    def is_full(self):
        """
        A tree is a full binary tree if each node is either a leaf or has degree exactly 2.
        :return: True - tree is full
                 False - tree is not full
        """
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            if not curr.is_a_leaf() and not curr.degree() == 2:
                return False
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return True

    def is_complete(self):
        """
        A complete binary tree is a binary tree in which all leaves have the same depth
        and all internal nodes have degree 2.
        :return: True - tree is complete
                 False - tree is not complete
        """

        # def _preorder(curr):
        #     nonlocal d
        #     if curr.is_a_leaf():
        #         if d == -1:
        #             d = self.tree_depth(curr)
        #         else:
        #             if self.tree_depth(curr) != d:
        #                 return False
        #     elif curr.degree() != 2:
        #         return False
        #     if curr.left:
        #         if not _preorder(curr.left):
        #             return False
        #     if curr.right:
        #         if not _preorder(curr.right):
        #             return False
        #     return True
        #
        # d = -1
        # return _preorder(self.root)

        stack = [self.root]
        d = -1
        while stack:
            curr = stack.pop()
            if curr.is_a_leaf():
                if d == -1:
                    d = self.tree_depth(curr)
                else:
                    if self.tree_depth(curr) != d:
                        return False
            elif curr.degree() != 2:
                return False
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return True

    @staticmethod
    def _tree_height(curr):
        """
        The height of a node in a tree is the number of edges on the longest simple
        downward path from the node to a leaf, and the height of a tree is the
        height of its root.

        :param curr: node of the tree
        :return: height of the node
        """

        def _tree_height_aux(curr, height):
            nonlocal max_height
            max_height = max(max_height, height)
            if curr.left:
                _tree_height_aux(curr.left, height + 1)
            if curr.right:
                _tree_height_aux(curr.right, height + 1)

        max_height = 0
        _tree_height_aux(curr, 0)
        return max_height

    def tree_height(self, key):
        curr = self._tree_search(self.root, key)
        return self._tree_height(curr)

    @staticmethod
    def tree_depth(curr):
        """
        The length of the simple path from the root r to a node x is the depth of x in tree T .

        :param curr:  node of the tree
        :return: depth of the node
        """
        if curr is None:
            return None

        depth = 0
        while curr.parent:
            depth += 1
            curr = curr.parent
        return depth

    @staticmethod
    def _tree_search(curr, key):
        while curr and curr.key != key:
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def tree_search(self, key):
        return bool(self._tree_search(self.root, key))

    # def tree_minimum(self, curr):
    #     if curr.left:
    #         return self.tree_minimum(curr.left)
    #     return curr

    @staticmethod
    def _tree_minimum(curr):
        while curr.left:
            curr = curr.left
        return curr

    def tree_minimum(self, key):
        curr = self._tree_search(self.root, key)
        return self._tree_minimum(curr).key

    # def tree_maximum(self, curr):
    #     if curr.right:
    #         return self.tree_maximum(curr.right)
    #     return curr

    @staticmethod
    def _tree_maximum(curr):
        while curr.right:
            curr = curr.right
        return curr

    def tree_maximum(self, key):
        curr = self._tree_search(self.root, key)
        return self._tree_maximum(curr).key

    def _tree_successor(self, curr):
        if curr is None:
            return None
        if curr.right is not None:
            return self._tree_minimum(curr.right)
        # go up the tree until we encounter a node that is the left child of its parent
        succ = curr.parent
        while succ and succ.right == curr:
            curr = succ
            succ = curr.parent
        return succ

    def tree_successor(self, key):
        curr = self._tree_search(self.root, key)
        succ = self._tree_successor(curr)
        return succ.key if succ else None

    def _tree_predecessor(self, curr):
        if curr is None:
            return None
        if curr.left is not None:
            return self._tree_maximum(curr.left)
        # go up the tree until we encounter a node that is the right child of its parent
        succ = curr.parent
        while succ and succ.left == curr:
            curr = succ
            succ = curr.parent
        return succ

    def tree_predecessor(self, key):
        curr = self._tree_search(self.root, key)
        pred = self._tree_predecessor(curr)
        return pred.key if pred else None

    def insert(self, new_key):
        curr = self.root
        parent = None

        while curr:
            parent = curr  # trailing pointer to parent
            if new_key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        new_node = Node(new_key)
        new_node.parent = parent
        if new_node.parent is None:
            self.root = new_node  # first node created is root
        else:
            if new_node.key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node

    def transplant(self, u, v):
        """
        Transplant replaces one subtree as a child of its parent with another subtree.
        When transplant replaces the subtree rooted at node u with the subtree rooted
        at node v, node u’s parent becomes node v’s parent, and u’s parent ends up having
        v as its appropriate child.

        :param u: node being replaced during transplant
        :param v: node which replaces u
        """
        if u.parent is None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def _tree_delete(self, curr):
        if curr is None:
            return
        if curr.left is None:
            self.transplant(curr, curr.right)
        elif curr.right is None:
            self.transplant(curr, curr.left)
        else:
            succ = self._tree_minimum(curr.right)
            if succ.parent != curr:
                self.transplant(succ, succ.right)
                succ.right = curr.right
                succ.right.parent = succ
            self.transplant(curr, succ)
            succ.left = curr.left
            succ.left.parent = succ

    def tree_delete(self, key):
        curr = self._tree_search(self.root, key)
        self._tree_delete(curr)

    # def delete(self, key):
    #     key, curr = self._search(key)
    #     if key is None:
    #         return None
    #
    #     if curr.has_no_left_child():
    #         self.transplant(curr, curr.right)
    #     elif curr.has_no_right_child():
    #         self.transplant(curr, curr.left)
    #     else:
    #         _, min_curr = self._find_min(curr.right)  # get min value from right child
    #         if min_curr.is_a_left_child():  # min will be removed from its left or right parent
    #             min_curr.parent.left = None
    #         elif min_curr.is_a_right_child():
    #             min_curr.parent.right = None
    #
    #         self.transplant(curr, min_curr)  # set the min in position of node which will be deleted
    #         min_curr.left = curr.left  # left and right of deleted node will be trasferred to min
    #         min_curr.right = curr.right
    #         if curr.left == min_curr:
    #             min_curr.left = None
    #         elif curr.right == min_curr:
    #             min_curr.right = None
    #
    # def transplant(self, curr, curr_trans):
    #     if curr.is_a_left_child():
    #         curr.parent.left = curr_trans
    #     elif curr.is_a_right_child():
    #         curr.parent.right = curr_trans
    #     else:
    #         self.root = curr_trans
    #         return
    #
    #     if curr_trans:
    #         curr_trans.parent = curr.parent

    # def search(self, key):
    #     return self._search(key)[0]
    #
    # def _search(self, key):
    #     curr, last_curr = self.root, None
    #     while curr:
    #         last_curr = curr  # used by insert
    #         if key == curr.key:
    #             return key, curr
    #         elif key < curr.key:
    #             curr = curr.left
    #         else:
    #             curr = curr.right
    #     return None, last_curr

    # def _tree_search(self, curr, key):
    #     if curr is None or curr.key == key:
    #         return curr
    #     if key < curr.key:
    #         return _self.tree_search(curr.left, key)
    #     else:
    #         return _self.tree_search(curr.right, key)

    # def _print_inorder(self, curr):
    #     if curr:
    #         self._print_inorder(curr.left)
    #         print(curr.key, end=' ')
    #         self._print_inorder(curr.right)
    # def print_inorder(self):
    #     self._print_inorder(self.root)
    #     print('')
    #

    # ------------------------------------------------------
    def print_inorder(self):
        def _print_inorder(curr):
            if curr.left:
                _print_inorder(curr.left)
            print(curr.key, end=' ')
            if curr.right:
                _print_inorder(curr.right)

        _print_inorder(self.root)
        print('')

    def inorder_arr(self):
        def _print_inorder(curr):
            if curr.left:
                _print_inorder(curr.left)
            inorder_arr.append(curr.key)
            if curr.right:
                _print_inorder(curr.right)

        inorder_arr = []
        _print_inorder(self.root)
        return inorder_arr

    def print_inorder_iter(self):
        curr = self.root
        stack = [curr]
        printed = set()
        while stack:
            if curr.left and curr.left not in printed:
                stack.append(curr)
                curr = curr.left
            elif curr not in printed:
                print(curr.key, end=' ')
                printed.add(curr)
            elif curr.right and curr.right not in printed:
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
        print('')

    def inorder_iter_arr(self):
        curr = self.root
        stack = [curr]
        printed = set()
        inorder_arr = []
        while stack:
            if curr.left and curr.left not in printed:
                stack.append(curr)
                curr = curr.left
            elif curr not in printed:
                inorder_arr.append(curr.key)
                printed.add(curr)
            elif curr.right and curr.right not in printed:
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
        return inorder_arr

    # ------------------------------------------------------
    def print_preorder(self):
        def _print_preorder(curr):
            print(curr.key, end=' ')
            if curr.left:
                _print_preorder(curr.left)
            if curr.right:
                _print_preorder(curr.right)

        _print_preorder(self.root)
        print('')

    def preorder_arr(self):
        def _preorder(curr):
            preorder_arr.append(curr.key)
            if curr.left:
                _preorder(curr.left)
            if curr.right:
                _preorder(curr.right)

        preorder_arr = []
        _preorder(self.root)
        return preorder_arr

    def print_preorder_iter(self):
        curr = self.root
        stack = [curr]
        printed = set()
        while stack:
            if curr not in printed:
                print(curr.key, end=' ')
                printed.add(curr)
            if curr.left and curr.left not in printed:
                stack.append(curr)
                curr = curr.left
            elif curr.right and curr.right not in printed:
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
        print('')

    def preorder_iter_arr(self):
        curr = self.root
        stack = [curr]
        printed = set()
        preorder_arr = []
        while stack:
            if curr not in printed:
                preorder_arr.append(curr.key)
                printed.add(curr)
            if curr.left and curr.left not in printed:
                stack.append(curr)
                curr = curr.left
            elif curr.right and curr.right not in printed:
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
        return preorder_arr

    # ------------------------------------------------------
    def print_postorder(self):
        def _print_postorder(curr):
            if curr.left:
                _print_postorder(curr.left)
            if curr.right:
                _print_postorder(curr.right)
            print(curr.key, end=' ')

        _print_postorder(self.root)
        print('')

    def postorder_arr(self):
        def _print_postorder(curr):
            if curr.left:
                _print_postorder(curr.left)
            if curr.right:
                _print_postorder(curr.right)
            postorder_arr.append(curr.key)

        postorder_arr = []
        _print_postorder(self.root)
        return postorder_arr

    def print_postorder_iter(self):
        curr = self.root
        stack = [curr]
        printed = []
        while stack:
            if curr.left and curr.left not in printed:
                stack.append(curr)
                curr = curr.left
            elif curr.right and curr.right not in printed:
                stack.append(curr)
                curr = curr.right
            elif curr not in printed:
                print(curr.key, end=' ')
                printed.append(curr)
            else:
                curr = stack.pop()
        print('')

    def postorder_iter_arr(self):
        curr = self.root
        stack = [curr]
        printed = []
        postorder_arr = []
        while stack:
            if curr.left and curr.left not in printed:
                stack.append(curr)
                curr = curr.left
            elif curr.right and curr.right not in printed:
                stack.append(curr)
                curr = curr.right
            elif curr not in printed:
                postorder_arr.append(curr.key)
                printed.append(curr)
            else:
                curr = stack.pop()
        return postorder_arr

    # def print_preorder(self):
    #     self._print_preorder(self.root)
    #     print('')
    #
    # def _print_preorder(self, curr):
    #     if curr:
    #         print(curr.key, end=' ')
    #         self._print_preorder(curr.left)
    #         self._print_preorder(curr.right)

    # def _print_preorder(self, curr):
    #     print curr.key,
    #     if curr.left is not None:
    #         self._print_preorder(curr.left)
    #     if curr.right is not None:
    #         self._print_preorder(curr.right)

    # def print_preorder_iterative(self):
    #     curr, seen = self.root, set()
    #     stack = [curr]
    #     while stack:
    #         curr = stack.pop()
    #         print(curr.key, end=' ')
    #         seen.add(curr.key)
    #         if curr == self.root:
    #             if curr.right:
    #                 stack.append(curr.right)
    #         else:
    #             if curr.is_a_leaf():
    #                 curr = curr.parent
    #         if curr.left and curr.left.key not in seen:
    #             stack.append(curr.left)
    #         elif curr.right and curr.right != self.root.right and curr.right.key not in seen:
    #             stack.append(curr.right)
    #     print('')

    # def print_preorder_iterative(self):
    #     curr = self.root
    #     stack = [self.root]
    #     seen = set()
    #     while stack:
    #         while curr.key in seen:
    #             curr = stack.pop()
    #         print(curr.key, end=' ')
    #         seen.add(curr.key)
    #         while curr.left:
    #             stack.append(curr.left)
    #             print(curr.left.key, end=' ')
    #             seen.add(curr.left.key)
    #             curr = curr.left
    #         if curr.parent.right:
    #             stack.append(curr.parent.right)
    #     print('')

    # def print_preorder_iterative(self):
    #     curr = self.root
    #     stack = [curr]
    #     visited = []
    #     while stack:
    #         if curr not in visited:
    #             print(curr.key, end=' ')
    #             visited.append(curr)
    #         if curr.left and curr.left not in visited:
    #             stack.append(curr.left)
    #             curr = curr.left
    #         elif curr.right and curr.right not in visited:
    #             stack.append(curr.right)
    #             curr = curr.right
    #         else:
    #             stack.pop()
    #             if stack:
    #                 curr = stack[-1]

    # def print_preorder_iterative(self):
    #     curr = self.root
    #     stack = [curr]
    #     printed = []
    #     while stack:
    #         if curr not in printed:
    #             print(curr.key, end=' ')
    #             printed.append(curr)
    #         if curr.left and curr.left not in printed:
    #             stack.append(curr)
    #             curr = curr.left
    #         elif curr.right and curr.right not in printed:
    #             stack.append(curr)
    #             curr = curr.right
    #         else:
    #             curr = stack.pop()
    #     print('')

    # def print_preorder_iterative(self):
    #     stack = [self.root]
    #     while stack:
    #         curr = stack.pop()
    #         print(curr.key, end=' ')
    #         if curr.right is not None:
    #             stack.append(curr.right)
    #         if curr.left is not None:
    #             stack.append(curr.left)
    #     print('')

    # def print_postorder(self):
    #     self._print_postorder(self.root)
    #     print('')
    #
    # def _print_postorder(self, curr):
    #     if curr:
    #         self._print_postorder(curr.left)
    #         self._print_postorder(curr.right)
    #         print(curr.key, end=' ')

    # def _print_postorder(self, curr):
    #     if curr.left is not None:
    #         self._print_postorder(curr.left)
    #     if curr.right is not None:
    #         self._print_postorder(curr.right)
    #     print curr.key,

    # def print_postorder_iterative(self):
    #     curr = self.root
    #     stack = [curr]
    #     seen = set()
    #     while stack:
    #         if curr.left and curr.left.key not in seen:
    #             stack.append(curr.left)
    #             curr = curr.left
    #         elif curr.right and curr.right.key not in seen:
    #             stack.append(curr.right)
    #             curr = curr.right
    #         else:
    #             print(curr.key, end=' ')
    #             seen.add(curr.key)
    #             curr = stack.pop().parent
    #             if stack:
    #                 if curr.right and curr.right.key not in seen:
    #                     stack.append(curr.right)
    #                     curr = curr.right
    #     print('')

    # def print_postorder_iterative(self):
    #     curr = self.root
    #     stack = [curr]
    #     visited = []
    #     while stack:
    #         if curr.left and curr.left not in visited:
    #             stack.append(curr.left)
    #             curr = curr.left
    #         elif curr.right and curr.right not in visited:
    #             stack.append(curr.right)
    #             curr = curr.right
    #         else:
    #             if curr not in visited:
    #                 print(curr.key, end=' ')
    #                 visited.append(curr)
    #                 stack.pop()
    #                 if stack:
    #                     curr = stack[-1]
    #     print('')

    # def print_postorder_iterative(self):
    #     curr = self.root
    #     stack = [curr]
    #     printed = []
    #     while stack:
    #         if curr.left and curr.left not in printed:
    #             stack.append(curr)
    #             curr = curr.left
    #         elif curr.right and curr.right not in printed:
    #             stack.append(curr)
    #             curr = curr.right
    #         else:
    #             print(curr.key, end=' ')
    #             printed.append(curr)
    #             curr = stack.pop()
    #     print('')

    def print_postorder_iterative(self):
        stack = [self.root]
        print_stack = []
        while stack:
            curr = stack.pop()
            print_stack.append(curr.key)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        while print_stack:
            print(print_stack.pop(), end=' ')
        print('')

    def print_level_order(self):
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            print(curr.key, end=' ')
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print('')

    def print_all_level_order(self):
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            print(f'key: {curr.key}  left: {curr.left}  right: {curr.right}')
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print('')

    # def print_level_order(self):
    #     curr = self.root
    #     node_queue = [curr]
    #     while node_queue:
    #         print curr.key,
    #         if curr.left is not None:
    #             node_queue.append(curr.left)
    #         if curr.right is not None:
    #             node_queue.append(curr.right)
    #         node_queue.pop(0)
    #         if node_queue:
    #             curr = node_queue[0]
    #     print ''

    # def print_level_order_recur(self):
    #     self._print_level_order_recur(self.root)
    #     print('')
    #
    # def _print_level_order_recur(self, curr):
    #     print(curr.key, end=' ')
    #     if curr.left:
    #         self._print_level_order_recur(curr.left)
    #     if curr.right:
    #         self._print_level_order_recur(curr.right)

    # def print_level_order_recur(self):
    #     self._print_level_order_recur(self.root, self.root.left, self.root.right)
    #
    # def _print_level_order_recur(self, curr, left, right):
    #     print curr.key,
    #     if curr.left is not None:
    #         if curr.left.is_a_leaf():
    #             print curr.left.key,
    #         else:
    #             self._print_level_order_recur(curr.left, curr.left.left, curr.left.right)
    #     if curr.right is not None:
    #         if curr.right.is_a_leaf():
    #             print curr.right.key,
    #         else:
    #             self._print_level_order_recur(curr.right, curr.right.left, curr.right.right)

    def print_tree_structure(self):
        self._print_tree_structure(self.root, 0)

    def _print_tree_structure(self, curr, level):
        if level == 0:
            print(curr.key)
        else:
            print('   ' * (level - 1) + '|___' + str(curr.key))

        if curr.left:
            self._print_tree_structure(curr.left, level + 1)

        if curr.right:
            self._print_tree_structure(curr.right, level + 1)

    def to_array(self):
        def _to_array(curr, arr):
            if curr:  # inorder
                _to_array(curr.left, arr)
                arr.append(curr.key)
                _to_array(curr.right, arr)

        arr = []
        _to_array(self.root, arr)
        return arr

    def right_rotate(self, key):
        _, y = self._search(key)
        x = y.left
        # y.right ==> no change
        y.left = x.right
        if y.left is not None:
            y.left.parent = y

        x.right = y
        x.parent = y.parent
        if x.parent is None:
            self.root = x
        elif x.parent.right == y:
            x.parent.right = x  # x is a right child
        else:
            x.parent.left = x  # x is a left child
        # x.left ==> no change
        y.parent = x  # should be last statement

    def left_rotate(self, key):
        _, x = self._search(key)
        y = x.right

        # x.left ==> no change
        x.right = y.left
        if x.right is not None:
            x.right.parent = x

        y.left = x
        # y.right ==> no change
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        elif y.parent.left == x:
            y.parent.left = y  # y is a left child
        else:
            y.parent.right = y  # y is a right child child

        x.parent = y.parent  # should be last statement


if __name__ == '__main__':
    # bst = BinarySearchTree()
    # bst.insert(4)
    # bst.insert(2)
    # bst.insert(6)
    # bst.insert(1)
    # bst.insert(3)
    # bst.insert(5)
    # bst.insert(7)
    # bst.insert(7)

    # bst.insert(1)
    # bst.insert(2)
    # bst.insert(3)
    # bst.insert(4)
    # bst.insert(5)
    # bst.insert(6)
    # bst.insert(7)
    # bst.insert(8)
    # bst.insert(9)
    # bst.insert(10)

    # print('inorder')
    # bst.print_inorder()
    # # bst.print_inorder_iterative()
    #
    # print('preorder')
    # bst.print_preorder()
    # bst.print_preorder_iterative()
    #
    # print('postorder')
    # bst.print_postorder()
    # bst.print_postorder_iterative()
    #
    # print('level order')
    # bst.print_level_order()
    # bst.print_level_order_recur()

    # print 'tree structure'
    # bst.print_tree_structure()
    #
    # print 'min', bst.find_min()
    # print 'max', bst.find_max()
    # print('search 5', bst.search(5))
    # print('search 20', bst.search(20))
    # print 'search', bst.search(8)

    # print('depth', bst.depth(4))
    # print('depth', bst.depth(2))
    # print('depth', bst.depth(6))
    # print('depth', bst.depth(1))
    # print('depth', bst.depth(3))
    # print('depth', bst.depth(5))
    # print('depth', bst.depth(7))
    # print('depth', bst.depth(99))

    # print
    # '=' * 8 + ' Successor ' + '=' * 8
    # print
    # bst.successor(1)
    # print
    # bst.successor(2)
    # print
    # bst.successor(3)
    # print
    # bst.successor(4)
    # print
    # bst.successor(5)
    # print
    # bst.successor(6)
    # print
    # bst.successor(7)
    # print
    # bst.successor(8)
    #
    # print
    # '=' * 8 + ' Predecessor ' + '=' * 8
    # print
    # bst.predecessor(1)
    # print
    # bst.predecessor(2)
    # print
    # bst.predecessor(3)
    # print
    # bst.predecessor(4)
    # print
    # bst.predecessor(5)
    # print
    # bst.predecessor(6)
    # print
    # bst.predecessor(7)
    # print
    # bst.predecessor(8)

    # print '=' * 32
    # print bst.search(1)
    # print bst.search(2)
    # print bst.search(3)
    # print bst.search(4)
    # print bst.search(5)
    # print bst.search(6)
    # print bst.search(7)
    # print bst.search(8)
    #
    # print '=' * 32
    # print bst.depth(4)
    # print bst.depth(2)
    # print bst.depth(6)
    # print bst.depth(1)
    # print bst.depth(3)
    # print bst.depth(5)
    # print bst.depth(7)
    # print bst.depth(8)

    # print
    # '=' * 8 + ' Convert to array ' + '=' * 8
    # print
    # bst.to_array()
    #
    # print
    # bst.height()

    # print(bst)
    # bst.delete(6)
    # bst.print_level_order()
    # bst.print_inorder()
    # print(bst.is_valid_bst())

    # print(bst)

    # bst = BinarySearchTree()
    # bst.insert(8)
    # bst.insert(4)
    # bst.insert(12)
    # bst.insert(2)
    # bst.insert(6)
    # bst.insert(10)
    # bst.insert(14)
    # bst.insert(1)
    # bst.insert(3)
    # bst.insert(5)
    # bst.insert(7)
    # bst.insert(9)
    # bst.insert(11)
    # bst.insert(13)
    # bst.insert(15)
    #
    # # bst.print_inorder()
    # # bst.print_preorder()  # 8 4 2 1 3 6 5 7 12 10 9 11 14 13 15
    # # bst.right_rotate(4)
    # # bst.print_preorder()  # 8 2 1 4 3 6 5 7 12 10 9 11 14 13 15
    # # bst.left_rotate(2)
    # # bst.print_preorder()  # 8 4 2 1 3 6 5 7 12 10 9 11 14 13 15 back to original
    # #
    # # bst.right_rotate(8)
    # # bst.print_preorder()  # 4 2 1 3 8 6 5 7 12 10 9 11 14 13 15
    # # bst.left_rotate(4)
    # # bst.print_preorder()  # 8 4 2 1 3 6 5 7 12 10 9 11 14 13 15 back to original
    # # print(bst.preorder())  # 8 4 2 1 3 6 5 7 12 10 9 11 14 13 15 back to original
    #
    # bst.print_inorder()
    #
    # # x = bst.tree_minimum(bst.root)
    # # print(x)
    # # x = bst.tree_minimum(bst.tree_search(bst.root, 4))
    # # print(x)
    # # x = bst.tree_minimum(bst.tree_search(bst.root, 2))
    # # print(x)
    # # x = bst.tree_minimum(bst.tree_search(bst.root, 1))
    # # print(x)
    # # x = bst.tree_minimum(bst.tree_search(bst.root, 3))
    # # print(x)
    # #
    # # x = bst.tree_minimum(bst.tree_search(bst.root, 6))
    # # print(x)
    # # x = bst.tree_minimum(bst.tree_search(bst.root, 5))
    # # print(x)
    # # x = bst.tree_minimum(bst.tree_search(bst.root, 7))
    # # print(x)
    # #
    # # print('-----')
    # # x = bst.tree_maximum(bst.root)
    # # print(x)
    # # x = bst.tree_maximum(bst.tree_search(bst.root, 4))
    # # print(x)
    # # x = bst.tree_maximum(bst.tree_search(bst.root, 10))
    # # print(x)
    # # x = bst.tree_maximum(bst.tree_search(bst.root, 7))
    # # print(x)
    # # x = bst.tree_maximum(bst.tree_search(bst.root, 13))
    # # print(x)
    #
    # print('-----')
    # print(bst._tree_successor(bst.root))
    # print(bst._tree_successor(bst._tree_search(bst.root, 4)))
    # print(bst._tree_successor(bst._tree_search(bst.root, 6)))
    # print(bst.root.is_a_leaf())
    # print(bst._tree_search(bst.root, 1).is_a_leaf())
    # print(bst.tree_depth(bst.root))
    # print(bst.tree_depth(bst._tree_search(bst.root, 4)))
    # print(bst.tree_depth(bst._tree_search(bst.root, 10)))
    # print(bst.tree_depth(bst._tree_search(bst.root, 13)))
    #
    # print('degree')
    # print(bst.root.degree())
    # print(bst._tree_search(bst.root, 1).degree())
    # bst.print_inorder()
    # bst.print_level_order()
    # print(bst.is_complete())
    #
    # bst = BinarySearchTree()  # clrs Figure 12.2
    # bst.insert(15)
    # bst.insert(6)
    # bst.insert(18)
    # bst.insert(3)
    # bst.insert(7)
    # bst.insert(17)
    # bst.insert(20)
    # bst.insert(2)
    # bst.insert(4)
    # bst.insert(13)
    # bst.insert(9)
    #
    # print(bst.tree_height(15))
    # print(bst.tree_successor(20))
    #
    # bst = BinarySearchTree()
    # print('insert')
    # bst.tree_insert(2)
    # bst.print_inorder()
    # bst.tree_insert(1)
    # bst.print_inorder()
    # bst.tree_insert(3)

    bst = BinarySearchTree()
    bst.insert(8)
    bst.insert(4)
    bst.insert(12)
    bst.insert(2)
    bst.insert(6)
    bst.insert(10)
    bst.insert(14)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    bst.insert(7)
    bst.insert(9)
    bst.insert(11)
    bst.insert(13)
    bst.insert(15)
    bst.print_inorder()

    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(2)
    bst.print_all_level_order()
    bst.tree_delete(5)
    bst.print_all_level_order()

    print('-----')
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(8)
    bst.print_all_level_order()
    bst.tree_delete(5)
    bst.print_all_level_order()

    print('-----')
    bst = BinarySearchTree()
    bst.insert(8)
    bst.insert(4)
    bst.insert(12)
    bst.insert(2)
    bst.insert(6)
    bst.insert(10)
    bst.insert(14)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    bst.insert(7)
    bst.insert(9)
    bst.insert(11)
    bst.insert(13)
    bst.insert(15)

    bst.print_preorder()
    bst.print_preorder_iter()
    print(bst.preorder_arr())
    print(bst.preorder_iter_arr())

    bst.print_inorder()
    bst.print_inorder_iter()
    print(bst.inorder_arr())
    print(bst.inorder_iter_arr())

    bst.print_postorder()
    bst.print_postorder_iter()
    print(bst.postorder_arr())
    print(bst.postorder_iter_arr())

