# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


t1 = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=TreeNode(4),
        right=TreeNode(5)
    ),
    right=TreeNode(
        val=3,
        right=TreeNode(6)
    )
)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def rec(tree: TreeNode):
            if tree:
                rec(tree.left)
                res.append(tree.val)
                rec(tree.right)

        rec(root)
        return res


print(Solution().inorderTraversal(t1))  # [4, 2, 5, 1, 3, 6]
