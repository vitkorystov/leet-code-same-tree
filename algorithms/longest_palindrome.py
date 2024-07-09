#  https://leetcode.com/problems/longest-palindrome/
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        res = 0
        odd_in = False
        for counter in d.values():
            if counter % 2 == 0:
                res += counter
            else:
                res += counter - 1
                odd_in = True
        return res + int(odd_in)


print(Solution().longestPalindrome("abccccdd"))  # 7
