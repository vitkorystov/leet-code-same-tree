#  https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t_map = dict()
        t_s_map = dict()
        res = True
        for s_char, t_char in zip(s, t):
            if s_char not in s_t_map and t_char not in t_s_map:
                s_t_map[s_char] = t_char
                t_s_map[t_char] = s_char
                continue
            if (s_char in s_t_map and t_char != s_t_map[s_char]) or s_char not in s_t_map:
                res = False
                break
        return res


print(Solution().isIsomorphic('foo', 'bar'))  # False
print(Solution().isIsomorphic('foo', 'egg'))  # True
print(Solution().isIsomorphic('badc', 'baba'))  # False
