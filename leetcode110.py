"""
110. Balanced Binary Tree
    Given a binary tree, determine if it is height-balanced.
    A height-balanced binary tree is a binary tree in which
    the depth of the two subtrees of every node never differs by more than one.

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: true

    Example 2:
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false

    Example 3:
    Input: root = []
    Output: true
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode) -> bool:
    """
    start time: 15:00
    end time: 16: 30
    method complexity: Runtime 43 ms; Memory 18.7 MB
    """
    if root is not None:
        if traversal(root) == -1:
            return False
    return True


def traversal(cur: TreeNode) -> int:
    if cur.left is not None:
        if traversal(cur.left) == -1:
            return -1
    if cur.right is not None:
        if traversal(cur.right) == -1:
            return -1
    find_depth(cur)
    if check(cur) == -1:
        return -1
    return 1


def find_depth(cur: TreeNode):
    if cur.left is None and cur.right is None:
        cur.depth = 0
    elif cur.left is not None and cur.right is not None:
        cur.depth = max(cur.left.depth, cur.right.depth) + 1
    else:
        node = cur.left or cur.right
        cur.depth = node.depth + 1


def check(cur: TreeNode) -> int:
    l = cur.left.depth + 1 if cur.left else 0
    r = cur.right.depth + 1 if cur.right else 0
    if abs(l - r) > 1:
        return -1
    return 1


if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print('actual {} expected True'.format(is_balanced(root)))

    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    print('actual {} expected False'.format(is_balanced(root)))

    root = None
    print('actual {} expected True'.format(is_balanced(root)))

    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(2, right=TreeNode(3, right=TreeNode(4))))
    print('actual {} expected False'.format(is_balanced(root)))
