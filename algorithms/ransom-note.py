# https://leetcode.com/problems/ransom-note/description/
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d_ransom = defaultdict(int)
        d_magazine = defaultdict(int)
        for l in ransomNote:
            d_ransom[l] += 1
        for l in magazine:
            d_magazine[l] += 1
        for l in d_ransom.keys():
            if l not in d_magazine or d_ransom[l] > d_magazine[l]:
                return False
        return True
