# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        max_len = max(len(a), len(b))

        res = ''
        add = 0

        max_number = None
        if len(a) > len(b):
            max_number = a
        elif len(b) > len(a):
            max_number = b

        for i in range(1, max_len+1):
            res_digit = 0
            if i <= len(b) and i <= len(a):
                a_digit = int(a[-i])
                b_digit = int(b[-i])

                if a_digit == 0 and b_digit == 0:
                    res_digit = 0 + add
                    add = 0
                if a_digit == 1 and b_digit == 1:
                    res_digit = 0 + add
                    add = 1
                if a_digit + b_digit == 1:
                    if add == 0:
                        res_digit = 1
                    else:
                        res_digit = 0
                        add = 1
            else:
                digit = int(max_number[-i])
                if digit == 0:
                    res_digit = add
                    add = 0
                else:
                    if add == 0:
                        res_digit = 1
                    else:
                        res_digit = 0
                        add = 1
            res = str(res_digit) + res

        if add == 1:
            res = '1' + res

        return res


print(Solution().addBinary(a="101111", b="10"))  # 110001
