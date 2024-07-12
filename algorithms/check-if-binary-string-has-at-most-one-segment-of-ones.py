# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        is_1st_batch_break = False
        for n in s:
            if n == '0' and not is_1st_batch_break:
                is_1st_batch_break = True
                continue
            if is_1st_batch_break and n == '1':
                return False
        return True


print(Solution().checkOnesSegment('110'))

