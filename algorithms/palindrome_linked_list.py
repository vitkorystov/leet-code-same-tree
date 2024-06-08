# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(val=1,
                  next=ListNode(
                      val=2,
                      next=ListNode(
                          val=2,
                          next=ListNode(
                              val=1,
                          )
                      )
                  )
              )


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        current_node = head
        while current_node:
            values.append(current_node.val)
            current_node = current_node.next

        reversed_values = list(reversed(values))
        return reversed_values == values


print(Solution().isPalindrome(l1))  # True

