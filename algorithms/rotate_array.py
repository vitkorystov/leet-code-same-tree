#  https://leetcode.com/problems/rotate-array/description/
from copy import deepcopy
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        target_k = k % len(nums) if k > len(nums) else k
        nums_copy = deepcopy(nums)
        length = len(nums)

        for i in range(length):
            new_i = i-target_k
            nums[i] = nums_copy[new_i]


Solution().rotate([1,2,3,4,5,6,7], 3)  # nums=[5,6,7,1,2,3,4]
