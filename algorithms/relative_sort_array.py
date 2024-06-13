#  https://leetcode.com/problems/relative-sort-array/

from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        rest = []
        d = {v: [] for i, v in enumerate(arr2)}
        for el1 in arr1:
            if el1 in arr2:
                d[el1].append(el1)
            else:
                rest.append(el1)
        for el2 in arr2:
            res.extend(d[el2])
        rest.sort()
        res.extend(rest)
        return res


print(Solution().relativeSortArray(
    [2,3,1,3,2,4,6,7,9,2,19],
    [2,1,4,3,9,6])
)  # [2,2,2,1,4,3,3,9,6,7,19]

print(Solution().relativeSortArray(
    [28,6,22,8,44,17],
    [22,28,8,6])
)  #  [22,28,8,6,17,44]