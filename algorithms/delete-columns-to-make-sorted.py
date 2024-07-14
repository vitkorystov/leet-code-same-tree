# https://leetcode.com/problems/delete-columns-to-make-sorted/
from collections import defaultdict


class Solution:
    def minDeletionSize(self, strs) -> int:

        grid = defaultdict(str)
        for word in strs:
            for i, c in enumerate(word):
                grid[i] += c

        counter = 0
        for col in grid.values():
            direct_sorted = ''.join(sorted(col))
            if col != direct_sorted:
                counter += 1
        return counter


print(Solution().minDeletionSize(["cba", "daf", "ghi"]))