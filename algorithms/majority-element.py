# https://leetcode.com/problems/majority-element/
from typing import List


nums_example = [-1, 1, 1, 1, 2, 1]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        first_element = nums[0]
        last_element = nums[-1]
        if len(nums) % 2 == 1:  # odd list length
            middle_element = nums[len(nums) // 2]
            if first_element == middle_element:
                return first_element
            elif last_element == middle_element:
                return last_element
            else:
                return middle_element
        else:   # even list length
            left_middle_element = nums[int(len(nums) / 2 - 1)]
            right_middle_element = nums[int(len(nums) / 2)]
            if first_element == left_middle_element:
                return first_element
            elif last_element == right_middle_element:
                return last_element
            else:
                return right_middle_element


print(Solution().majorityElement(nums_example))  # 1
