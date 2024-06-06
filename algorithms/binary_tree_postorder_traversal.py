# https://leetcode.com/problems/binary-tree-postorder-traversal/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


t1 = TreeNode(
    val=1,
    left=TreeNode(2),
    right=TreeNode(
        val=3,
        left=TreeNode(4),
        right=TreeNode(5)
    )
)


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def rec(tree):
            if tree:
                rec(tree.left)
                rec(tree.right)
                res.append(tree.val)

        if root:
            rec(root)
        return res


print(Solution().postorderTraversal(t1))  # [2, 4, 5, 3, 1]



