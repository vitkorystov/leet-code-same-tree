# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List


class Solution(object):
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sums = 0
        d = {0: 1}
        for n in nums:
            prefix_sums += n
            res += d.get(prefix_sums - k, 0)
            d[prefix_sums] = d.get(prefix_sums, 0) + 1
        return res


print(Solution().subarraySum([1, -1, 0], 0))  # 3
print(Solution().subarraySum([1, 1, 1], 2))   # 2
print(Solution().subarraySum([1, 2, 3], 3))   # 2
print(Solution().subarraySum([-1, -1, 1], 0))
