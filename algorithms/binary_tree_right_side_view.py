# https://leetcode.com/problems/binary-tree-right-side-view/
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


t2 = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
    )
)


t3 = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=TreeNode(4)
    ),
    right=TreeNode(3)
)


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res_dict = dict()
        level = 0

        def rec(tree: TreeNode, _level):
            if tree:
                if _level in res_dict:
                    res_dict[_level].append(tree.val)
                else:
                    res_dict[_level] = [tree.val]
                _level += 1
                rec(tree.right, _level)
                rec(tree.left, _level)

        if root:
            rec(root, level)

        return [
            v[0]
            for v in res_dict.values()
        ]


print(Solution().rightSideView(t1))  # [1, 3, 5]
print(Solution().rightSideView(t2))  # [1, 2]
print(Solution().rightSideView(t3))  # [1, 3, 4]
