# https://leetcode.com/problems/word-pattern/description/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(pattern) != len(s_list):
            return False
        p_word_map = dict()
        word_p_map = dict()
        for p, word in zip(pattern, s_list):
            if p not in p_word_map:
                p_word_map[p] = word
            if word not in word_p_map:
                word_p_map[word] = p
            if p_word_map[p] != word or word_p_map[word] != p:
                return False
        return True


print(Solution().wordPattern("abba", "dog cat cat dog"))  # True
print(Solution().wordPattern("abba", "dog dog dog dog"))  # False
print(Solution().wordPattern("abc", "dog cat dog"))  # False
