# https://leetcode.com/problems/binary-search/submissions/1219250763/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        min_pos = 0
        max_pos = len(nums)

        while min_pos < max_pos:
            midpoint = int(min_pos + (max_pos - min_pos) / 2)

            if nums[midpoint] > target:
                max_pos = midpoint
            elif nums[midpoint] < target:
                min_pos = midpoint + 1
            else:
                return midpoint
        
        return -1