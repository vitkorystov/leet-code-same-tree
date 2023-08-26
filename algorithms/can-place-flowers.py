# https://leetcode.com/problems/can-place-flowers/
from typing import List


l = [1, 0, 0, 0, 0, 1]

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cells = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            cells += 1
            return cells >= n
        else:
            for i, el in enumerate(flowerbed):
                if el == 0:
                    if (i == 0 and flowerbed[i+1] == 0
                            or (i == len(flowerbed) - 1 and flowerbed[i-1] == 0)
                            or (flowerbed[i - 1] == 0 and flowerbed[i+1] == 0)):
                        cells += 1
                        flowerbed[i] = 1
                if cells == n:
                    return True
            return cells >= n


print(Solution().canPlaceFlowers(l, 1))  # True
