# https://leetcode.com/problems/generate-parentheses/
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        s = set()

        def rec(st: str, left, right):
            if len(st) == n * 2:
                s.add(st)
                return
            if left < n:
                rec(st+'(', left+1, right)
            if right < left:
                rec(st + ')', left, right+1)

        rec('', 0, 0)
        return list(s)


print(Solution().generateParenthesis(3))