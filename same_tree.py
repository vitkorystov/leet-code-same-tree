# https://leetcode.com/problems/same-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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

        for i1, i2 in zip(tree_iteration(p), tree_iteration(q)):
            if i1 != i2:
                return False
        return True
