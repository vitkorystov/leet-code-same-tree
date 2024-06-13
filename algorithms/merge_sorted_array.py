# https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(len(nums1)-m):
            nums1.pop()
        for i in range(len(nums2)-n):
            nums2.pop()

        nums1.extend(nums2)
        nums1.sort()




Solution().merge(
[1, 2, 3, 0, 0, 0],
    3,
[2, 5, 6],
    3
)
