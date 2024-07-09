# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i = -1
        res = ""
        add = 0
        while -i <= len(num1) or -i <= len(num2):

            n1 = num1[i] if -i <= len(num1) else None
            n2 = num2[i] if -i <= len(num2) else None

            if n1 and n2:
                sum_ = int(n1) + int(n2)
                if sum_ <= 9:
                    digit = sum_+add if sum_+add < 10 else 0
                    res = str(digit) + res
                    add = 0 if sum_+add < 10 else 1
                else:
                    res = str(int(str(sum_)[1]) + add) + res
                    add = 1
            elif None in [n1, n2]:
                digit = n1 or n2
                if int(digit) + add == 10:
                    res = str(0) + res
                    add = 1
                else:
                    res = str(int(digit) + add) + res
                    add = 0
            i -= 1

        if add == 1:
            res = str(add) + res
        return res


print(Solution().addStrings("11", "199"))  # 210
print(Solution().addStrings("1", "9"))  # 10
print(Solution().addStrings("584", "18"))  # 602
print(Solution().addStrings("6994", "36"))  # 7030