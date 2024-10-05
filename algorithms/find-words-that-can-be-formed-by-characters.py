# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
from copy import copy
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_list = [c for c in chars]
        res = 0
        for word in words:
            chars_list_copy = copy(chars_list)
            for c in word:
                if c in chars_list_copy:
                    chars_list_copy.remove(c)
                else:
                    break
            else:
                res += len(word)
        return res
