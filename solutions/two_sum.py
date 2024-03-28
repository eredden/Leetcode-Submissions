# https://leetcode.com/submissions/detail/1208643570/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}

        for idx in range(len(nums)):
            complement = target - nums[idx]

            if complement in num_map:
                return [num_map[complement], idx]

            num_map[nums[idx]] = idx
        
        return []