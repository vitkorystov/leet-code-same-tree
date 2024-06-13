# https://leetcode.com/problems/pascals-triangle/
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for lvl in range(1, numRows+1):
            lvl_list = []
            if lvl == 1:
                lvl_list.append(1)
            else:
                prev_lvl_list = res[lvl-2]
                for j in range(lvl):
                    if j == 0 or j == lvl-1:
                        v = 1
                    else:
                        v = prev_lvl_list[j-1] + prev_lvl_list[j]
                    lvl_list.append(v)
            res.append(lvl_list)
        return res
