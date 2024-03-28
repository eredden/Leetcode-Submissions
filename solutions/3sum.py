# https://leetcode.com/problems/3sum/submissions/1216472334

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answers = []
        nums.sort()

        for index, number in enumerate(nums):
            if index > 0 and number == nums[index - 1]:
                continue
            
            left = index + 1
            right = len(nums) - 1

            while left < right:
                threeSum = number + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    answers.append([number, nums[left], nums[right]])

                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return answers