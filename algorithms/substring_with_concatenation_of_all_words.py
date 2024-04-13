# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        max_s_length = word_len * len(words)
        res = []
        i = 0
        while True:
            if i > len(s) - word_len:
                break
            batch = s[i:i+word_len]
            if batch in words:
                assumed_s = s[i+word_len:i+max_s_length]
                batch_list = [assumed_s[j: j+word_len] for j in range(0, len(assumed_s), word_len)]
                batch_list.append(batch)
                if sorted(batch_list) == sorted(words):
                    res.append(i)
            i += 1
        return res


print(Solution().findSubstring('barfoothefoobarman', ["foo", "bar"]))  # [0,9]
print(Solution().findSubstring("aaaaaaaaaaaaaa", ["aa","aa"]))  # [0,1,2,3,4,5,6,7,8,9,10]
print(Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))  # [6,9,12]
print(Solution().findSubstring('wordgoodgoodgoodbestword', ["word", "good", "best", "word"]))  # []
print(Solution().findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))  # [6,9,12]
