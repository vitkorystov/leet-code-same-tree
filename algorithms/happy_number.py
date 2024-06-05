# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        numbers_list = [int(el) for el in str(n)]
        s_list = []
        while True:
            s = sum(el**2 for el in numbers_list)
            if s == 1:
                return True
            numbers_list = [int(el) for el in str(s)]
            if s in s_list:
                return False
            s_list.append(s)


assert Solution().isHappy(19) is True
assert Solution().isHappy(191) is False
