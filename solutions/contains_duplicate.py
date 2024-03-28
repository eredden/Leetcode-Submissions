# https://leetcode.com/submissions/detail/1208613483/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        distinct = {}

        for num in nums:
            if num in distinct:
                return True
            
            distinct[num] = num

        return False