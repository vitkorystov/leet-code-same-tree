# https://leetcode.com/problems/binary-tree-paths/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def rec(tree, s=''):
            if tree:
                new_s = s + str(tree.val) + '->'
                rec(tree.left, new_s)
                rec(tree.right, new_s)
                if tree.left is None and tree.right is None:
                    res.append(s + str(tree.val))

        rec(root)
        return res


print(Solution().binaryTreePaths(
    TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4)),
        right=TreeNode(3, left=TreeNode(6), right=TreeNode(7))
        )
    )
)  # ['1->2->4', '1->3->6', '1->3->7']
