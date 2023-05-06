# https://leetcode.com/problems/symmetric-tree/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(
    val=1,
    left=TreeNode(val=2,
                  left=TreeNode(val=3, left=TreeNode(val=5), right=TreeNode(val=6)),
                  right=TreeNode(val=4, left=TreeNode(val=7), right=TreeNode(val=8)),
                  ),

    right=TreeNode(val=2,
                   left=TreeNode(val=4, left=TreeNode(val=8), right=TreeNode(val=7)),
                   right=TreeNode(val=3, left=TreeNode(val=6), right=TreeNode(val=5)),
                   ),
)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        left_tree = root.left
        right_tree = root.right

        if left_tree is None and right_tree is None:
            return True
        if left_tree is None and right_tree is not None:
            return False
        if left_tree is not None and right_tree is None:
            return False

        def tree_iteration(tree: TreeNode):
            is_level_0 = True
            level_nodes = []
            while True:
                if is_level_0:
                    level_nodes = [tree]
                    is_level_0 = False
                else:
                    l = []
                    for node in level_nodes:
                        if node is None:
                            l.extend([None, None])
                        else:
                            l.append(node.left if node.left is not None else None)
                            l.append(node.right if node.right is not None else None)
                    level_nodes = l
                yield list(map(lambda x: None if x is None else x.val, level_nodes))
                if len(set(level_nodes)) == 1 and level_nodes[0] is None:
                    break

        for i1, i2 in zip(tree_iteration(left_tree), tree_iteration(right_tree)):
            if i1 != list(reversed(i2)):
                return False
        return True


res = Solution().isSymmetric(tree)
print(res)  # True
