# https://leetcode.com/problems/powx-n/
from functools import reduce


class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        x = x if n > 0 else 1/x

        if n == 1:
            return x

        target = []

        def rec(x_,  current_i, last_i, p):
            nonlocal target
            if current_i < p:
                new_current_i = current_i * 2
                if new_current_i > p:
                    target.append(x_)
                x_ = x_ * x_
                rec(x_, new_current_i, current_i, p)
            elif current_i > p:
                new_p = p - last_i
                rec(x, 1, 1, new_p)
            else:
                target.append(x_)

        rec(x, 1, 1, abs(n))

        res = reduce(lambda a, b:  a*b, target)
        return res


print('res', Solution().myPow(3, 5))  # 243
