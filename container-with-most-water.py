# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 1
        right = len(height)
        area_current = 0
        while left < right:
            area = (right - left) * min([height[right-1], height[left-1]])
            if area > area_current:
                area_current = area
            if height[left-1] < height[right-1]:
                left += 1
            else:
                right -= 1
        return area_current
