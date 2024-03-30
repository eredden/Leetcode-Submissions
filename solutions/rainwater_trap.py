# https://leetcode.com/problems/trapping-rain-water/submissions/1218268378/

class Solution:
    def trap(self, height: list[int]) -> int:        
        water = 0
        l_ptr, r_ptr = 0, len(height) - 1
        l_max, r_max = height[l_ptr], height[r_ptr]

        while l_ptr < r_ptr:
            if r_max > l_max:
                l_ptr += 1
                l_max = max(l_max, height[l_ptr])
                water += l_max - height[l_ptr]
            else:
                r_ptr -= 1
                r_max = max(r_max, height[r_ptr])
                water += r_max - height[r_ptr]

        return water