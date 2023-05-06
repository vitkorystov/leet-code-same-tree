# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l = ListNode(val=1,
             next=ListNode(val=1,
                           next=ListNode(val=2,
                                         next=ListNode(val=3,
                                                       next=ListNode(val=3, next=None)
                                                       )
                                         )
                           )
             )


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current_node = head
        new_unique_list = []
        new_linked_list = None
        new_linked_list_current_element = None
        while True:
            current_node_val = current_node.val
            if new_linked_list is None:
                new_linked_list = ListNode(val=current_node_val)
                new_linked_list_current_element = new_linked_list
                new_unique_list.append(current_node_val)
            if current_node_val not in new_unique_list:
                new_unique_list.append(current_node_val)
                new_linked_list_current_element.next = ListNode(val=current_node_val)
                new_linked_list_current_element = new_linked_list_current_element.next
            if current_node.next is None:
                break
            current_node = current_node.next
        return new_linked_list


res = Solution().deleteDuplicates(l)
print(res.val)              # 1
print(res.next.val)         # 2
print(res.next.next.val)    # 3
print(res.next.next.next)   # None
