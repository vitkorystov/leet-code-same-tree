# https://leetcode.com/problems/reverse-linked-list/description/

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
                          val=3,
                          next=ListNode(
                              val=4,
                              next=ListNode(
                                  val=5,
                              )
                          )
                      )
                  )
              )

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current_node = head
        while current_node:
            values.append(current_node.val)
            current_node = current_node.next

        i = 0
        values.reverse()
        current_node_2 = head
        while current_node_2:
            current_node_2.val = values[i]
            current_node_2 = current_node_2.next
            i += 1
        return head


res_list = Solution().reverseList(l1)
print(res_list.val)  # 5
print(res_list.next.val)  # 4
