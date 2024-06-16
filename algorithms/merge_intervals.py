# https://leetcode.com/problems/merge-intervals/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        d = dict()
        for i, interval in enumerate(intervals):
            start = interval[0]
            end = interval[1]
            if i == 0:
                for j in range(start, end+1):
                    d[j] = interval
            else:
                for j in range(start, end+1):
                    if j in d:
                        prev_interval = d[j]
                        new_start = min(prev_interval[0], interval[0])
                        new_end = max(prev_interval[1], interval[1])
                        new_interval = [new_start, new_end]

                        if prev_interval[0] < interval[0]:
                            for k in range(prev_interval[0], interval[0]):
                                d[k] = new_interval

                        if interval[1] > prev_interval[1]:
                            for k in range(prev_interval[1], interval[1]+1):
                                d[k] = new_interval
                        d[j] = new_interval
                    else:
                        d[j] = interval

        res = []
        for interval in d.values():
            if interval not in res:
                res.append(interval)
        return res


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1, 6], [8, 10], [15, 18]]
print(Solution().merge([[1,4],[0,1]]))
