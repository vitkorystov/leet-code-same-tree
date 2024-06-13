# https://leetcode.com/problems/minimum-depth-of-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        lvl_list = []

        def rec(tree, lvl: int):
            if tree:
                if tree.left is None and tree.right is None:
                    lvl_list.append(lvl)
                    return
                rec(tree.right, lvl + 1)
                rec(tree.left, lvl + 1)

        rec(root, 1)
        return min(lvl_list) if lvl_list else 0
