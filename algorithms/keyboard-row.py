# https://leetcode.com/problems/keyboard-row/description/
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = {
            0: "qwertyuiop",
            1: "asdfghjkl",
            2: "zxcvbnm"
        }
        res = []
        for word in words:
            target = set()
            for letter in word:
                for k, v in keyboard.items():
                    if letter.lower() in v:
                        target.add(k)
                        break
                if len(target) > 1:
                    break
            else:
                res.append(word)
        return res


print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))  # ["Alaska","Dad"]