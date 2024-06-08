# https://leetcode.com/problems/remove-linked-list-elements/

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
                      val=6,
                      next=ListNode(
                          val=3,
                          next=ListNode(
                              val=4,
                              next=ListNode(val=6)
                          )
                      )
                  )
              )
              )


l2 = ListNode(val=7,
              next=ListNode(
                  val=7,
                  next=ListNode(
                      val=7,
                      next=ListNode(
                          val=7,
                      )
                  )
              )
              )


l3 = ListNode(val=1,
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        custom_node = head
        while custom_node:
            if head is None:
                break
            if head.val == val:
                head = head.next
                continue

            if custom_node.next and custom_node.next.val == val:
                custom_node.next = custom_node.next.next
                continue
            custom_node = custom_node.next
        return head


res_node = (Solution().removeElements(l3, 2))
print(res_node.val)  # 1
print(res_node.next.val)  # 1


res_node = (Solution().removeElements(l2, 7))
print(res_node)  # None


res_node = (Solution().removeElements(l1, 6))
print(res_node.val)  # 1
print(res_node.next.val)  # 2
print(res_node.next.next.val)  # 3
print(res_node.next.next.next.val)  # 4
print(res_node.next.next.next.next)  # None
