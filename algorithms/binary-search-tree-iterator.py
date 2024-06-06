from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


r1 = TreeNode(
    val=7,
    left=TreeNode(3),
    right=TreeNode(
        val=15,
        left=TreeNode(9),
        right=TreeNode(20)
    )
)


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        def rec(tree: TreeNode):
            if tree:
                self.stack.append(tree.val)
                rec(tree.left)
                rec(tree.right)

        rec(root)

        self.stack.sort()
        self.pointer = 0

    def next(self) -> int:
        res = self.stack[self.pointer]
        self.pointer += 1
        return res

    def hasNext(self) -> bool:
        return self.pointer < len(self.stack)


obj = BSTIterator(r1)
param_1 = obj.next()
param_2 = obj.hasNext()