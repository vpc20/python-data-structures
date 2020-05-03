from RandomBinarySearchTree import random_bst


def height(node):
    left = 0
    right = 0
    if node.left:
        left = 1 + height(node.left)
    if node.right:
        right = 1 + height(node.right)
    return max(left, right)


def heightx(node):
    def heightx_aux(node):
        if node is None:
            return 0
        left = 1 + heightx_aux(node.left)
        right = 1 + heightx_aux(node.right)
        return max(left, right)

    return heightx_aux(node) - 1


def height_dfs(node):
    def dfs(node, h):
        nonlocal maxh
        if node.left is None and node.right is None:
            maxh = max(maxh, h)
            return
        if node.left:
            dfs(node.left, h + 1)
        if node.right:
            dfs(node.right, h + 1)

    maxh = 0
    dfs(node, 0)
    return maxh


for i in range(1000):
    bst = random_bst()
    bst.print_preorder()
    assert height(bst.root) == height_dfs(bst.root)
    # print(height(bst.root))
    # print(heightx(bst.root))
    assert height(bst.root) == heightx(bst.root)
