# https://leetcode.com/submissions/detail/1209556486/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answers = [1] * len(nums)

        end = len(nums) - 1
        prefix  = 1
        postfix = 1

        for index in range(0, end):
            prefix *= nums[index]
            answers[index + 1] = prefix

        for index in range(end, 0, -1):
            postfix *= nums[index]
            answers[index - 1] *= postfix

        return answers