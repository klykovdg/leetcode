"""
700. Search in a Binary Search Tree
    You are given the root of a binary search tree (BST) and an integer val.
    Find the node in the BST that the node's value equals val
    and return the subtree rooted with that node.
    If such a node does not exist, return null.

    Example 1:
    Input: root = [4,2,7,1,3], val = 2
    Output: [2,1,3]

    Example 2:
    Input: root = [4,2,7,1,3], val = 5
    Output: []
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search(root: TreeNode, val: int) -> TreeNode | None:
    """
    start time: 19:24
    end time: 19:38
    method complexity: Runtime 78 ms; Memory 16.4 MB
    """
    if root is not None:
        if root.val == val:
            return root
        return traversal(root, val)
    return None


def traversal(cur: TreeNode, val: int):
    for node in cur.left, cur.right:
        if node is not None:
            if node.val == val:
                return node

    for node in cur.left, cur.right:
        if node is not None:
            result = traversal(node, val)
            if result is not None:
                return result
