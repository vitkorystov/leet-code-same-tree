# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        batch_length = len(nums)

        def get_batch(batch: tuple, rest: tuple):
            for el in rest:
                new_batch = list(batch)
                new_batch.append(el)
                if len(new_batch) == batch_length:
                    res.append(new_batch)
                    return
                else:
                    new_rest = list(rest)
                    new_rest.remove(el)
                    get_batch(tuple(new_batch), tuple(new_rest))

        get_batch(tuple(), tuple(nums))
        return res


print(Solution().permute([1, 2, 3]))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(Solution().permute([0, 1]))  # [[0,1],[1,0]]
print(Solution().permute([1]))  # [[1]]
