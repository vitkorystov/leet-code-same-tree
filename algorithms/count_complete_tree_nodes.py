# https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


example_root = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=TreeNode(val=4),
        right=TreeNode(val=5)
    ),
    right=TreeNode(
        val=3,
        left=TreeNode(val=6)
    )
)


class Solution(object):
    def countNodes(self, root):
        counter = 0
        def rec(tree):
            nonlocal counter
            if tree:
                print(tree.val)
                counter += 1
                rec(tree.left)
                rec(tree.right)

        rec(root)
        return counter


print('res =', Solution().countNodes(example_root))  # res = 6
