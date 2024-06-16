# https://leetcode.com/problems/path-sum-ii/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path_list = []

        def rec(tree, l):
            if tree:
                if l is None:
                    new_l = [tree.val]
                else:
                    new_l = [i for i in l]
                    new_l.append(tree.val)
                if tree.left is None and tree.right is None:
                    path_list.append(new_l)
                else:
                    rec(tree.left, new_l)
                    rec(tree.right, new_l)

        rec(root, None)
        return [row for row in path_list if sum(row) == targetSum]


assert Solution().pathSum(
    TreeNode(5,
             left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))),
             right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, left=TreeNode(5), right=TreeNode(1))),
             ),
    22
) == [[5, 4, 11, 2], [5, 8, 4, 5]]