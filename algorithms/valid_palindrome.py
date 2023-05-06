# https://leetcode.com/problems/valid-palindrome/

s1 = "A man, a plan, a canal: Panama"


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_index = 0
        s = list(map(lambda x: x.lower(), s))
        s = ''.join(filter(lambda x: x.isalpha() or x.isnumeric(), s))
        right_index = len(s) - 1
        if len(s) == 1:
            return True
        result = True
        while left_index < right_index:
            left_letter = s[left_index]
            right_letter = s[right_index]
            if left_letter != right_letter:
                return False
            left_index += 1
            right_index -= 1
        return result


res = Solution().isPalindrome(s1)
print(res)  # True
