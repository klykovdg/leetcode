"""
617. Merge Two Binary Trees
    You are given two binary trees root1 and root2.
    Imagine that when you put one of them to cover the other,
    some nodes of the two trees are overlapped while the others are not.
    You need to merge the two trees into a new binary tree.
    The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
    Otherwise, the NOT null node will be used as the node of the new tree.
    Return the merged tree.
    Note: The merging process must start from the root nodes of both trees.

    Example 1:
    Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
    Output: [3,4,5,5,4,null,7]

    Example 2:
    Input: root1 = [1], root2 = [1,2]
    Output: [2,2]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        result = [self.val]
        print_traversal(self, result)

        return str(result)


def print_traversal(cur: TreeNode, result: list):
    if cur.left:
        result.append(cur.left.val)
    if cur.right:
        result.append(cur.right.val)
    if cur.left:
        print_traversal(cur.left, result)
    if cur.right:
        print_traversal(cur.right, result)


def merge_trees(root1: TreeNode, root2: TreeNode):
    """
    start time: 13:30
    end time: 14:23
    method complexity: Runtime 97 ms; Memory 15.8 MB
    """
    if root1 and root2:
        result = TreeNode()
        result.val = root1.val + root2.val
        traversal(result, root1, root2)
        return result
    else:
        return root1 or root2


def traversal(result_cur, cur1, cur2):
    do_node(result_cur, cur1.left, cur2.left, True)
    do_node(result_cur, cur1.right, cur2.right, False)

    if cur1.left and cur2.left:
        traversal(result_cur.left, cur1.left, cur2.left)
    if cur1.right and cur2.right:
        traversal(result_cur.right, cur1.right, cur2.right)


def do_node(result_cur: TreeNode, cur1: TreeNode, cur2: TreeNode, is_left):
    if is_left:
        if cur1 and cur2:
            result_cur.left = TreeNode(cur1.val + cur2.val)
        else:
            cur = cur1 or cur2
            if cur:
                result_cur.left = TreeNode(cur.val)
                copy_traversal(result_cur.left, cur)
    else:
        if cur1 and cur2:
            result_cur.right = TreeNode(cur1.val + cur2.val)
        else:
            cur = cur1 or cur2
            if cur:
                result_cur.right = TreeNode(cur.val)
                copy_traversal(result_cur.right, cur)


def copy_traversal(result_cur: TreeNode, cur: TreeNode):
    if cur.left:
        result_cur.left = TreeNode(cur.left.val)
    if cur.right:
        result_cur.right = TreeNode(cur.right.val)
    if cur.left:
        copy_traversal(result_cur.left, cur.left)
    if cur.right:
        copy_traversal(result_cur.right, cur.right)


if __name__ == '__main__':
    root1 = TreeNode(1, TreeNode(3, left=TreeNode(5)), TreeNode(2))
    root2 = TreeNode(2, TreeNode(1, right=TreeNode(4)), TreeNode(3, right=TreeNode(7)))
    print('actual {} expected [3, 4, 5, 5, 4, 7]'.format(merge_trees(root1, root2)))

    root1 = TreeNode(1)
    root2 = TreeNode(1, TreeNode(2))
    print('actual {} expected [2, 2]'.format(merge_trees(root1, root2)))

    root1 = TreeNode(3, TreeNode(4, left=TreeNode(1), right=TreeNode(2)), TreeNode(5))
    root2 = TreeNode(4, TreeNode(1, TreeNode(1)), TreeNode(2))
    print('actual {} expected [7, 5, 7, 2, 2]'.format(merge_trees(root1, root2)))
