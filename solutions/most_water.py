# https://leetcode.com/submissions/detail/1214602808/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0

        while i < j:
            area = min(height[j],  height[i]) * abs(j - i)
            max_area = area if area > max_area else max_area

            if height[j] > height[i]:
                i += 1
            else:
                j -= 1

        return max_area