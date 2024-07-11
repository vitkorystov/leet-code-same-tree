# https://leetcode.com/problems/split-linked-list-in-parts/
from copy import deepcopy
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=ListNode(
            val=3,
            next=ListNode(
                val=4,
                next=ListNode(
                    val=5,
                    next=None
                )
            )
        )
    )
)


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        values_list = []
        node = head
        while node is not None:
            values_list.append(node.val)
            node = node.next

        # build nodes list
        N = len(values_list)
        batch_length_list = [N//k for _ in range(k)]
        for i in range(N % k):
            batch_length_list[i] += 1

        res = []
        i = 0
        for batch_length in batch_length_list:
            root = None
            for _ in range(batch_length):
                temp = ListNode(values_list[i])
                if root is None:
                    root = temp
                else:
                    ptr = root
                    while ptr.next != None:
                        ptr = ptr.next
                    ptr.next = temp
                i += 1
            res.append(root)
        return res


Solution().splitListToParts(l, 2)
