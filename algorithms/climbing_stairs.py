# https://leetcode.com/problems/climbing-stairs/description/


class Solution:
    def climbStairs(self, n: int) -> int:
        prev_2 = 1  # for n=1 count=1:  (1)
        prev = 2    # for n=2 count=2: (1+1), (2)
        for lvl in range(2, n):
            current = prev_2 + prev
            prev_2, prev = prev, current
        return prev if n > 1 else 1


print(Solution().climbStairs(5))

