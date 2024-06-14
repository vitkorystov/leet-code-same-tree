# https://leetcode.com/problems/merge-two-binary-trees/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


t1 = TreeNode(
    1,
    left=TreeNode(3, left=TreeNode(5)),
    right=TreeNode(2),
)

t2 = TreeNode(
    2,
    left=TreeNode(1, right=TreeNode(4)),
    right=TreeNode(3, right=TreeNode(7)),
)


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(r1: Optional[TreeNode], r2: Optional[TreeNode]):
            if r1 is None:
                return r2
            if r2 is None:
                return r1
            r1.val += r2.val
            r1.left = rec(r1.left, r2.left)
            r1.right = rec(r1.right, r2.right)
            return r1

        res_tree = rec(root1, root2)
        return res_tree


res = Solution().mergeTrees(t1, t2)
print(res.val)  # 3
print(res.left.val)  # 4
print(res.right.val)  # 5
print(res.left.left.val)  # 5
print(res.left.right.val)   # 4
print(res.right.right.val)   # 7


res2 = Solution().mergeTrees(None, TreeNode(1))
print(res2.val)  # 1


res3 = Solution().mergeTrees(
    TreeNode(1, left=TreeNode(2, left=TreeNode(3))),
    TreeNode(1, right=TreeNode(2, right=TreeNode(3)))
)
print(res3.val)  # 2
print(res3.left.val)  # 2
print(res3.right.val)  # 2
print(res3.left.left.val)  # 3
print(res3.right.right.val)  # 3
