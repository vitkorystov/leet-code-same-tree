# https://leetcode.com/problems/power-of-two/


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1:
            return True

        res: bool = False

        def rec(left: int, right: int, base: int):
            nonlocal res
            attempt = 2**base
            if attempt > n:
                new_base = (left + base) / 2
                right = base
                if abs(left-right) != 1:
                    rec(left, right, new_base)
            elif attempt < n:
                new_base = (right + base) / 2
                left = base
                if abs(left - right) != 1:
                    rec(left, right, new_base)
            else:
                res = True

        rec(0, 32, 2)

        return res


print(Solution().isPowerOfTwo(5))


