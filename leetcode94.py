"""
94. Binary Tree Inorder Traversal
    Given the root of a binary tree, return the inorder traversal of its nodes' values.

    Example 1:
    Input: root = [1,null,2,3]
    Output: [1,3,2]

    Example 2:
    Input: root = []
    Output: []

    Example 3:
    Input: root = [1]
    Output: [1]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode):
    """
    start time: 19:45
    end time: 20:00
    method complexity: Runtime 34 ms; Memory 13.8 MB
    """
    result = []
    if root:
        result.append(root.val)
        traversal(root, result)
    return result


def traversal(cur: TreeNode, result: list):
    if cur.left:
        traversal(cur.left, result)
    result.append(cur.val)
    if cur.right:
        traversal(cur.right, result)
