# https://leetcode.com/problems/valid-anagram/description/
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def convert_to_dict(target_str: str) -> dict[str, int]:
            d = defaultdict(int)
            for letter in target_str:
                d[letter] += 1
            return d

        return convert_to_dict(s) == convert_to_dict(t)


print(Solution().isAnagram("anagram", "nagaram"))  # True
