# https://leetcode.com/problems/balanced-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


t1 = TreeNode(
    val=3,
    left=TreeNode(9),
    right=TreeNode(
        val=20,
        left=TreeNode(15),
        right=TreeNode(7)
    )
)


t2 = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=TreeNode(
            val=3,
            left=TreeNode(val=4),
            right=TreeNode(val=4)
        ),
        right=TreeNode(val=3)
    ),
    right=TreeNode(val=2)
)

t3 = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=TreeNode(
            val=4,
            left=TreeNode(val=8),
        ),
        right=TreeNode(val=5)
    ),
    right=TreeNode(val=3, left=TreeNode(val=6))
)

t4 = TreeNode(
    val=1,
    right=TreeNode(
        val=2,
        right=TreeNode(3)
    )
)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_depth(tree):
            max_d = 0

            def foo(tree, d=1):
                nonlocal max_d
                if tree:
                    if d > max_d:
                        max_d = d
                    foo(tree.left, d + 1)
                    foo(tree.right, d + 1)

            foo(tree)
            return max_d

        res = True

        def rec(tree: TreeNode):
            nonlocal res
            if tree:
                left_d = get_depth(tree.left)
                right_d = get_depth(tree.right)
                if abs(left_d - right_d) > 1:
                    res = False
                rec(tree.left)
                rec(tree.right)

        rec(root)

        return res


print(Solution().isBalanced(t1))  # True
print(Solution().isBalanced(t2))  # False
print(Solution().isBalanced(t3))  # True
print(Solution().isBalanced(t4))  # False