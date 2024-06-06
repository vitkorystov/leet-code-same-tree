# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


r1 = TreeNode(
    val=1,
    left=TreeNode(2),
    right=TreeNode(
        val=3,
        left=TreeNode(4),
        right=TreeNode(5)
    )
)


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []

        def rec(tree: TreeNode):
            if tree:
                res.append(tree.val)
                rec(tree.left)
                rec(tree.right)
        if root:
            rec(root)

        return res


print(Solution().preorderTraversal(r1))  # [1, 2, 3, 4, 5]




