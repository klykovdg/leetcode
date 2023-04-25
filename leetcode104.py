"""
104. Maximum Depth of Binary Tree
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path
    from the root node down to the farthest leaf node.

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

    Example 2:
    Input: root = [1,null,2]
    Output: 2
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode):
    """
    start time: 20:53
    end time: 21:05
    method complexity: Runtime 42 ms; Memory 16.4 MB
    """
    if root:
        max_dep = [1,]
        depth = 1
        traversal(root, depth, max_dep)
        return max_dep[0]
    return 0


def traversal(cur: TreeNode, depth, max_dep):
    if cur.left:
        traversal(cur.left, depth + 1, max_dep)
    if depth > max_dep[0]:
        max_dep[0] = depth
    if cur.right:
        traversal(cur.right, depth + 1, max_dep)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    print('actual {} expected 3'.format(max_depth(root)))

    root = TreeNode(1, right=TreeNode(2))
    print('actual {} expected 2'.format(max_depth(root)))
