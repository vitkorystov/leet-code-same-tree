# https://leetcode.com/problems/invert-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


example_root = TreeNode(
    val=4,
    left=TreeNode(
        val=2,
        left=TreeNode(val=1),
        right=TreeNode(val=3)
    ),
    right=TreeNode(
        val=7,
        left=TreeNode(val=6),
        right=TreeNode(val=9)
    )
)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def change_branch(tree: TreeNode):
            if tree:
                tree.left, tree.right = tree.right, tree.left
                change_branch(tree.left)
                change_branch(tree.right)

        change_branch(root)
        return root


res = Solution().invertTree(example_root)

print(res.val)                                                                            #         4
print(res.left.val, res.right.val)                                                        #    7         2
print(res.left.left.val, res.left.right.val, res.right.left.val, res.right.right.val)     # 9    6    3     1






