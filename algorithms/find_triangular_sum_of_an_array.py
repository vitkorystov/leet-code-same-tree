# https://leetcode.com/problems/find-triangular-sum-of-an-array/description/

from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = 0

        def rec(n_list: list[int]):
            nonlocal res
            new_list = []
            for i, n in enumerate(n_list):
                if i+1 < len(n_list):
                    s = (n+n_list[i+1]) % 10
                    new_list.append(s)
            if len(new_list) == 1:
                res = new_list[0]
            else:
                rec(new_list)
        if len(nums) == 1:
            return nums[0]
        rec(nums)
        return res



print(Solution().triangularSum([1,2,3,4,5]))  # 8
print(Solution().triangularSum([5]))  # 5
