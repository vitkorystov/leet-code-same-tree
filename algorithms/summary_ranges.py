# https://leetcode.com/problems/summary-ranges/
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        start_num = None
        for i, num in enumerate(nums):
            if i == 0:
                start_num = num
                if len(nums) == 1:
                    res.append(str(start_num))
                continue
            prev_num = nums[i-1]
            if num - prev_num == 1:
                if i == len(nums) - 1:
                    end_num = num
                    res_str = f'{start_num}->{end_num}' if start_num != end_num else str(start_num)
                    res.append(res_str)
            else:
                end_num = prev_num
                res_str = f'{start_num}->{end_num}' if start_num != end_num else str(start_num)
                res.append(res_str)
                start_num = num

                if i == len(nums) - 1:
                    end_num = num
                    res_str = f'{start_num}->{end_num}' if start_num != end_num else str(start_num)
                    res.append(res_str)

        return res

print(Solution().summaryRanges([0,1,2,4,5,7]))  # ["0->2","4->5","7"]
print(Solution().summaryRanges([0,2,3,4,6,8,9]))  # ["0","2->4","6","8->9"]
print(Solution().summaryRanges([1]))  # ['1']