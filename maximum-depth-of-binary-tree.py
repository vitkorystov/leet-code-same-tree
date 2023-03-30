# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(
    val=1,
    left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)),
    right=TreeNode(val=3),
)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_level = 1
        
        def traversal(node: TreeNode, level):
            nonlocal max_level
            if node is not None:
                if level > max_level:
                    max_level = level
                traversal(node.left, level + 1)
                traversal(node.right, level + 1)

        traversal(root, 1)
        return max_level


res = Solution().maxDepth(tree)
print(res)  # 3
