# https://leetcode.com/problems/valid-anagram/description/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def convert_to_dict(target_str: str) -> dict[str, int]:
            d = dict()
            for letter in target_str:
                if letter not in d:
                    d[letter] = 0
                else:
                    d[letter] += 1
            return d

        return convert_to_dict(s) == convert_to_dict(t)
