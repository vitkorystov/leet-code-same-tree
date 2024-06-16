# https://leetcode.com/problems/find-the-middle-index-in-array/description/
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i, n in enumerate(nums):
            left_sum = left_sum + nums[i - 1] if i - 1 >= 0 else left_sum
            right_sum -= n
            if left_sum == right_sum:
                return i
        return -1
