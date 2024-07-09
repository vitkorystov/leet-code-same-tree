#  https://leetcode.com/problems/pascals-triangle-ii/
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []

        def rec(n, row_list):
            nonlocal res
            l = [1]
            for i, number in enumerate(row_list):
                if i + 1 < len(row_list):
                    l.append(number + row_list[i + 1])
            l.append(1)
            if n < rowIndex-1:
                rec(n + 1, l)
            else:
                res = l

        if rowIndex == 0:
            return [1]
        else:
            rec(0, [1])

        return res


print(Solution().getRow(2))  # [1, 2, 1]
