# https://leetcode.com/problems/zigzag-conversion/description/


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        res_dict: dict[int, list[str]] = dict()

        step = 2 * numRows - 2
        for i in range(0, len(s), step):
            for j in range(step):
                s_index = i + j
                if s_index > (len(s) - 1):
                    continue
                s_item = s[s_index]
                if j < numRows:
                    if j not in res_dict:
                        res_dict[j] = [s_item]
                    else:
                        res_dict[j].append(s_item)
                else:
                    key = step - j
                    res_dict[key].append(s_item)

        res_str = ''
        for li in res_dict.values():
            res_str += ''.join(li)

        return res_str


print(Solution().convert("A", 1))  # "A"
print(Solution().convert("PAYPALISHIRING", 3))  # "PAHNAPLSIIGYIR"
print(Solution().convert("PAYPALISHIRING", 4))  # "PINALSIGYAHRPI"
