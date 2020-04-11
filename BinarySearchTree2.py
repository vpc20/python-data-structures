class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

    def is_a_leaf(self):
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


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # def __str__(self):
    #     s = ''
    #     curr = self.root
    #     stack = []
    #     while stack or curr is not None:
    #         if curr is not None:
    #             stack.append(curr)
    #             curr = curr.left
    #         else:
    #             if stack:
    #                 curr = stack.pop()
    #                 s += str(curr.key) + ', '
    #                 curr = curr.right
    #     return '<BinarySearchTree> (' + s.rstrip(', ') + ')'

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
        stack = [self.root]
        while stack:
            curr = stack.pop()
            # print(curr.key, end=' ')
            # if curr.left is not None:
            #     print(curr.left.key, end=' ')
            # else:
            #     print('None', end=' ')
            # if curr.right is not None:
            #     print(curr.right.key)
            # else:
            #     print('None')
            if (curr.left is not None and curr.left.key > curr.key) \
                    or (curr.right is not None and curr.right.key < curr.key):
                return False
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return True

    # each node has exactly one or two children
    def is_full(self):
        pass

    # todo-me define is_full method in binary tree

    # completely filled with the exception of bottom level which is filled from left to right
    def is_complete(self):
        pass

    # todo-me define is_complete method in binary tree

    def height(self, key=None):
        if key is None:
            curr = self.root
        else:
            key, curr = self._search(key)
            if key is None:
                return None
        return self._height(curr) - 1

    def _height(self, curr):
        if curr is None:
            return 0
        return 1 + max(self._height(curr.left), self._height(curr.right))

    # def _height(self, curr):
    #     if curr is None:
    #         return 0
    #     lheight = self._height(curr.left)
    #     rheight = self._height(curr.right)
    #     if lheight > rheight:
    #         return 1 + lheight
    #     else:
    #         return 1 + rheight

    # def height(self, key=None):
    #     def incr_height(child_node, h, maxh):
    #         stack.append(child_node)
    #         h += 1
    #         maxh = max(maxh, h)
    #         return child_node, h, maxh
    #
    #     if key is None:
    #         curr = self.root
    #     else:
    #         _, curr = self._search(key)
    #         if curr is None:
    #             return None
    #
    #     h, maxh, stack, seen = 0, 0, [curr], set()
    #     while stack:
    #         if curr.left and curr.left.key not in seen:
    #             curr, h, maxh = incr_height(curr.left, h, maxh)
    #         elif curr.right and curr.right.key not in seen:
    #             curr, h, maxh = incr_height(curr.right, h, maxh)
    #         else:
    #             seen.add(curr.key)
    #             curr = stack.pop().parent
    #             h -= 1
    #             if stack:
    #                 if curr.right and curr.right.key not in seen:
    #                     curr, h, maxh = incr_height(curr.right, h, maxh)
    #     return maxh

    # the height of a node is the number of edges from the node to the deepest leaf
    # def height(self, key=None):
    #     if key is None:
    #         curr = self.root
    #     else:
    #         _, curr = self._search(key)
    #         if curr is None:
    #             return None
    #     h, maxh = 0, 0
    #     stack = [curr]
    #     seen = set()
    #     while stack:
    #         if curr.left is not None and curr.left.key not in seen:
    #             stack.append(curr.left)
    #             h += 1
    #             maxh = max(maxh, h)
    #             curr = curr.left
    #         elif curr.right is not None and curr.right.key not in seen:
    #             stack.append(curr.right)
    #             h += 1
    #             maxh = max(maxh, h)
    #             curr = curr.right
    #         else:
    #             # print curr.key,
    #             seen.add(curr.key)
    #             curr = stack.pop().parent
    #             h -= 1
    #             if stack:
    #                 if curr.right is not None and curr.right.key not in seen:
    #                     stack.append(curr.right)
    #                     h += 1
    #                     maxh = max(maxh, h)
    #                     curr = curr.right
    #     return maxh

    def depth(self, key):  # the depth of a node is the number of edges from the root to the node
        key, curr = self._search(key)
        if key is None:
            return None

        depth = 0
        while curr.parent:
            depth += 1
            curr = curr.parent
        return depth

    # def depth(self, key):  # the depth of a node is the number of edges from the root to the node
    #     _, curr = self._search(key)
    #     if curr is None:
    #         return None
    #     return self._depth(key, curr)
    #
    # def _depth(self, key, curr):
    #     if curr.parent is None:
    #         return 0
    #     else:
    #         return 1 + self._depth(key, curr.parent)

    def insert(self, new_key):
        if self.root is None:
            self.root = Node(new_key)
        else:
            self._insert(new_key, self.root)

    def _insert(self, new_key, curr):
        # while curr:
        #     last_curr = curr
        #     if new_key == curr.key:
        #         print('Duplicate key', str(curr.key), 'is not allowed for insert function')
        #         return
        #     elif new_key < curr.key:
        #         curr = curr.left
        #     else:
        #         curr = curr.right
        _, last_node = self._search(new_key)
        new_node = Node(new_key)
        new_node.parent = last_node
        if new_node.key < last_node.key:
            last_node.left = new_node
        else:
            last_node.right = new_node

    # def _insert(self, new_key, curr):
    #     if new_key == curr.key:
    #         print 'Duplicate key', str(curr.key), 'is not allowed for insert function'
    #     elif new_key < curr.key:
    #         if curr.left is None:
    #             new_node = Node(new_key)
    #             new_node.parent = curr
    #             curr.left = new_node
    #         else:
    #             self._insert(new_key, curr.left)
    #     else:
    #         if curr.right is None:
    #             new_node = Node(new_key)
    #             new_node.parent = curr
    #             curr.right = new_node
    #         else:
    #             self._insert(new_key, curr.right)

    def delete(self, key):
        key, curr = self._search(key)
        if key is None:
            return None

        if curr.has_no_left_child():
            self.transplant(curr, curr.right)
        elif curr.has_no_right_child():
            self.transplant(curr, curr.left)
        else:
            _, min_curr = self._find_min(curr.right)  # get min value from right child
            if min_curr.is_a_left_child():  # min will be removed from its left or right parent
                min_curr.parent.left = None
            elif min_curr.is_a_right_child():
                min_curr.parent.right = None

            self.transplant(curr, min_curr)  # set the min in position of node which will be deleted
            min_curr.left = curr.left  # left and right of deleted node will be trasferred to min
            min_curr.right = curr.right
            if curr.left == min_curr:
                min_curr.left = None
            elif curr.right == min_curr:
                min_curr.right = None

    def transplant(self, curr, curr_trans):
        if curr.is_a_left_child():
            curr.parent.left = curr_trans
        elif curr.is_a_right_child():
            curr.parent.right = curr_trans
        else:
            self.root = curr_trans
            return

        if curr_trans:
            curr_trans.parent = curr.parent

    def search(self, key):
        return self._search(key)[0]

    def _search(self, key):
        curr, last_curr = self.root, None
        while curr:
            last_curr = curr  # used by insert
            if key == curr.key:
                return key, curr
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return None, last_curr

    # def _search(self, key, curr):
    #     if curr is None:
    #         return None, None
    #     if key == curr.key:
    #         return key, curr
    #     elif key < curr.key:
    #         return self._search(key, curr.left)
    #     else:
    #         return self._search(key, curr.right)

    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root)[0]

    @staticmethod
    def _find_min(curr):
        while curr.left:
            curr = curr.left
        return curr.key, curr

    # def _find_min(self, curr):
    #     if curr.left is None:
    #         return curr.key
    #     else:
    #         return self._find_min(curr.left)

    def find_max(self):
        if self.root is None:
            return None
        return self._find_max(self.root)

    @staticmethod
    def _find_max(curr):
        while curr.right:
            curr = curr.right
        return curr.key

    # def _find_max(self, curr):
    #     if curr.right is None:
    #         return curr.key
    #     else:
    #         return self._find_max(curr.right)

    def successor(self, key):
        key, curr = self._search(key)
        if key is None:
            return None
        else:
            if curr.right:  # successor is the minimum key on the right node
                return self._find_min(curr.right)[0]
            else:
                parent = curr.parent
                while parent and parent.right == curr:
                    curr = parent
                    parent = curr.parent
                if parent is None:
                    return None
                else:
                    return parent.key

    def predecessor(self, key):
        key, curr = self._search(key)
        if key is None:
            return None
        else:
            if curr.left:  # predecessor is the maximum key on the left node
                return self._find_max(curr.left)
            else:
                parent = curr.parent
                while parent and parent.left == curr:
                    curr = parent
                    parent = curr.parent
                if parent is None:
                    return None
                else:
                    return parent.key

    def print_inorder(self):
        def _print_inorder(curr):
            if curr.left:
                _print_inorder(curr.left)
            print(curr.key, end=' ')
            if curr.right:
                _print_inorder(curr.right)

        _print_inorder(self.root)
        print('')

    # def print_inorder(self):
    #     self._print_inorder(self.root)
    #     print('')
    #
    # def _print_inorder(self, curr):
    #     if curr:
    #         self._print_inorder(curr.left)
    #         print(curr.key, end=' ')
    #         self._print_inorder(curr.right)

    # def _print_inorder(self, curr):
    #     if curr.left is not None:
    #         self._print_inorder(curr.left)
    #     print curr.key,
    #     if curr.right is not None:
    #         self._print_inorder(curr.right)

    # def print_inorder_iterative(self):
    #     curr = self.root
    #     stack = [self.root]
    #     seen = set()
    #     while stack:
    #         if curr.left and curr.left.key not in seen:
    #             stack.append(curr.left)
    #             curr = curr.left
    #         else:
    #             curr = stack.pop()
    #             print(curr.key, end=' ')
    #             seen.add(curr.key)
    #             if curr != self.root:
    #                 if curr and curr.parent.left == curr:
    #                     curr = stack.pop()
    #                     print(curr.key, end=' ')
    #                     seen.add(curr.key)
    #                 else:
    #                     curr = curr.parent
    #             if curr.right and curr.right.key not in seen:
    #                 stack.append(curr.right)
    #                 curr = curr.right
    #     print('')

    def print_inorder_iterative(self):
        curr = self.root
        stack = [curr]
        printed = []
        while stack:
            if curr.left and curr.left not in printed:
                stack.append(curr)
                curr = curr.left
            elif curr not in printed:
                print(curr.key, end=' ')
                printed.append(curr)
                curr = stack.pop()
                if curr.left in printed and curr not in printed:
                    print(curr.key, end=' ')
                    printed.append(curr)
                if curr.right and curr.right not in printed:
                    stack.append(curr)
                    curr = curr.right
                else:
                    curr = stack.pop()
        print('')

    # def print_inorder_iterative(self):
    #     curr = self.root
    #     stack = []
    #     while stack or curr:
    #         if curr:
    #             stack.append(curr)
    #             curr = curr.left
    #         else:
    #             curr = stack.pop()
    #             print(curr.key, end=' ')
    #             curr = curr.right
    #     print('')

    def print_preorder(self):
        def _print_preorder(curr):
            print(curr.key, end=' ')
            if curr.left:
                _print_preorder(curr.left)
            if curr.right:
                _print_preorder(curr.right)

        _print_preorder(self.root)
        print('')

    def preorder(self):
        def _preorder(curr):
            preorder_vertices.append(curr.key)
            if curr.left:
                _preorder(curr.left)
            if curr.right:
                _preorder(curr.right)

        preorder_vertices = []
        _preorder(self.root)
        return preorder_vertices

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

    def print_preorder_iterative(self):
        curr = self.root
        stack = [curr]
        printed = []
        while stack:
            if curr not in printed:
                print(curr.key, end=' ')
                printed.append(curr)
            if curr.left and curr.left not in printed:
                stack.append(curr)
                curr = curr.left
            elif curr.right and curr.right not in printed:
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
        print('')

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

    def print_postorder(self):
        def _print_postorder(curr):
            if curr.left:
                _print_postorder(curr.left)
            if curr.right:
                _print_postorder(curr.right)
            print(curr.key, end=' ')

        _print_postorder(self.root)
        print('')

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
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            print(curr.key, end=' ')
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

    def print_level_order_recur(self):
        self._print_level_order_recur(self.root)
        print('')

    def _print_level_order_recur(self, curr):
        print(curr.key, end=' ')
        if curr.left:
            self._print_level_order_recur(curr.left)
        if curr.right:
            self._print_level_order_recur(curr.right)

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
        arr = []
        self._to_array(self.root, arr)
        return arr

    def _to_array(self, curr, arr):
        if curr:
            self._to_array(curr.left, arr)
            arr.append(curr.key)
            self._to_array(curr.right, arr)

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
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(2)
    bst.insert(6)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    bst.insert(7)
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

    print('inorder')
    bst.print_inorder()
    bst.print_inorder_iterative()

    print('preorder')
    bst.print_preorder()
    bst.print_preorder_iterative()

    print('postorder')
    bst.print_postorder()
    bst.print_postorder_iterative()

    print('level order')
    bst.print_level_order()
    # bst.print_level_order_recur()

    # print 'tree structure'
    # bst.print_tree_structure()
    #
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

    print(bst)

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

    # bst.print_inorder()
    bst.print_preorder()  # 8 4 2 1 3 6 5 7 12 10 9 11 14 13 15
    bst.right_rotate(4)
    bst.print_preorder()  # 8 2 1 4 3 6 5 7 12 10 9 11 14 13 15
    bst.left_rotate(2)
    bst.print_preorder()  # 8 4 2 1 3 6 5 7 12 10 9 11 14 13 15 back to original

    bst.right_rotate(8)
    bst.print_preorder()  # 4 2 1 3 8 6 5 7 12 10 9 11 14 13 15
    bst.left_rotate(4)
    bst.print_preorder()  # 8 4 2 1 3 6 5 7 12 10 9 11 14 13 15 back to original
    print(bst.preorder())  # 8 4 2 1 3 6 5 7 12 10 9 11 14 13 15 back to original

    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(1)
    # bst.insert(2)
    print(bst)

    bst.tree_delete(5)
    print(bst)
