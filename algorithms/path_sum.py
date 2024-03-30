# https://leetcode.com/problems/path-sum/description/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(
    val=1,
    left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)),
    right=TreeNode(val=3, right=TreeNode(val=6)),
)


class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False

        node_sum_list = []

        def traversal(node: TreeNode, node_sum: int):
            nonlocal node_sum_list

            if node is not None:
                node_sum += node.val

                if node.left is None and node.right is None:

                    node_sum_list.append(node_sum)
                    if targetSum in node_sum_list:
                        return

                traversal(node.left, node_sum)
                traversal(node.right, node_sum)

        traversal(root, 0)

        return targetSum in node_sum_list


res_true = Solution().hasPathSum(tree, 8)
print(res_true)    # True

res_false = Solution().hasPathSum(tree, 11)
print(res_false)   # False
