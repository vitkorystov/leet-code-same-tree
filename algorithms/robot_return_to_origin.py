# https://leetcode.com/problems/robot-return-to-origin/


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        points = {
            'x': 0,
            'y': 0
        }
        moves_map = {
            "U": ('y', 1),
            'D': ('y', -1),
            'R': ('x', 1),
            'L': ('x', -1),
        }
        for move in moves:
            m = moves_map[move]
            points[m[0]] += m[1]
        return points['x'] == 0 and points['y'] == 0
