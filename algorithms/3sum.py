#  https://leetcode.com/problems/3sum/description/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                if temp_sum == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif temp_sum > 0:
                    right -= 1
                else:
                    left += 1
        return list(res)


print(Solution().threeSum([-1,0,1,2,-1,-2]))
