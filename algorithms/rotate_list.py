# https://leetcode.com/problems/rotate-list/
from copy import deepcopy
from typing import Optional


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
            next=None
        )
    )
)


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        def get_length():
            node = deepcopy(head)
            list_length = 0
            while node is not None:
                list_length += 1
                node = node.next
            return list_length

        l_length = get_length()

        def rotate():
            node = head
            prev = None
            while node is not None:
                current = deepcopy(node.val)
                node.val = prev
                prev = current
                node = node.next
            head.val = prev

        target_k = k % l_length if k > l_length else k

        for _ in range(target_k):
            rotate()

        return head


res = Solution().rotateRight(l, 2)
print(res.val)  # 2
print(res.next.val)  # 3
print(res.next.next.val)  # 1
