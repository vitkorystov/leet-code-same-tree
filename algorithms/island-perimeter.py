# https://leetcode.com/problems/island-perimeter/
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        grid_length = len(grid)
        res = 0
        for i, row in enumerate(grid):
            row_size = len(row)
            for j, cell in enumerate(row):
                if cell == 1:
                    # left and right check
                    if not (j-1 >= 0 and row[j-1] == 1):
                        res += 1
                    if not (j+1 <= row_size -1 and row[j+1] == 1):
                        res += 1
                    # up adn down check
                    if not( i-1 >= 0 and grid[i-1][j] == 1):
                        res += 1
                    if not (i+1 <= grid_length -1 and grid[i+1][j] == 1):
                        res += 1

        return res

print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))  # 16
