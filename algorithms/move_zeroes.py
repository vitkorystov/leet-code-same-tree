# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_counter = 0
        while True:
            if 0 in nums:
                nums.remove(0)
                zero_counter += 1
            else:
                break
        nums.extend([0 for _ in range(zero_counter)])

        print(nums)

Solution().moveZeroes([0, 1, 0, 3, 12])
Solution().moveZeroes([0,0,1])
