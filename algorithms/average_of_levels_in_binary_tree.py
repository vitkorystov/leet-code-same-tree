# https://leetcode.com/problems/average-of-levels-in-binary-tree/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        lvl_dict = dict()
        lvl_dict[0] = [root.val]

        def rec(tree, lvl=1):
            if tree:
                if lvl not in lvl_dict:
                    lvl_dict[lvl] = []
                if tree.left:
                    lvl_dict[lvl].append(tree.left.val)
                if tree.right:
                    lvl_dict[lvl].append(tree.right.val)

                rec(tree.left, lvl + 1)
                rec(tree.right, lvl + 1)

        rec(root)

        res = [sum(v) / len(v) for v in lvl_dict.values() if v]
        return res


print(Solution().averageOfLevels(
    TreeNode(val=3,
             left=TreeNode(9),
             right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
))  # [3.0, 14.5, 11.0]



print(Solution().averageOfLevels(
    TreeNode(val=3,
             left=TreeNode(9, left=TreeNode(15), right=TreeNode(7)),
             right=TreeNode(20)
)))  # [3.0, 14.5, 11.0]