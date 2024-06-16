# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        def get_values_as_int(linled_list) -> int:
            res = []
            current_node = linled_list
            while current_node:
                res.append(str(current_node.val))
                current_node = current_node.next
            res.reverse()
            return int(''.join(res))

        values_l1 = get_values_as_int(l1)
        values_l2 = get_values_as_int(l2)

        s = values_l1 + values_l2
        s = str(s)
        s = s[::-1]
        s_list = [int(el) for el in s]
        root = None
        for el in s_list:
            temp = ListNode(el)
            if root is None:
                root = temp
            else:
                ptr = root
                while ptr.next is not None:
                    ptr = ptr.next
                ptr.next = temp
        return root


Solution().addTwoNumbers(
    l1=ListNode(2, next=ListNode(4, next=ListNode(3))),
    l2=ListNode(5, next=ListNode(6, next=ListNode(4))),
)
