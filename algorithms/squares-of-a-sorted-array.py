# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        div_index = None
        is_all_neq = True
        for i in range(len(nums) - 1):
            if nums[i] < 0 and nums[i + 1] >= 0:
                div_index = i
                break

        for i in range(len(nums)):
            if nums[i] >= 0:
                is_all_neq = False

        if div_index is None and not is_all_neq:
            return [n ** 2 for n in nums]  # all pos
        elif is_all_neq:
            return [n ** 2 for n in sorted(nums, reverse=True)]  # all neq
        else:
            neq_array = sorted(nums[:div_index + 1], reverse=True)
            pos_array = nums[div_index + 1:]
            res = []
            pos_i = 0
            neq_i = 0
            while pos_i < len(pos_array) or neq_i < len(neq_array):
                if pos_i == len(pos_array):
                    res.append(neq_array[neq_i]**2)
                    neq_i += 1
                elif neq_i == len(neq_array):
                    res.append(pos_array[pos_i]**2)
                    pos_i += 1
                else:
                    if neq_array[neq_i] ** 2 < pos_array[pos_i] ** 2:
                        res.append(neq_array[neq_i] ** 2)
                        neq_i += 1
                    else:
                        res.append(pos_array[pos_i] ** 2)
                        pos_i += 1
            return res


print(Solution().sortedSquares([-4,-1,0,3,10]))
print(Solution().sortedSquares([-5,-3,-2,-1]))