# https://leetcode.com/problems/sorting-the-sentence/


class Solution:
    def sortSentence(self, s: str) -> str:
        d = dict()
        for word in s.split(" "):
            number = int(word[-1])
            d[number] = word[:len(word)-1]
        return " ".join([d[key] for key in sorted(d.keys())])


print(Solution().sortSentence("is2 sentence4 This1 a3"))
