# https://leetcode.com/submissions/detail/1212655901/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        num_ptr = 0
        com_ptr = len(numbers) - 1

        while num_ptr < com_ptr:
            if numbers[num_ptr] + numbers[com_ptr] > target:
                com_ptr -= 1
            elif numbers[num_ptr] + numbers[com_ptr] < target:
                num_ptr += 1
            else:
                return [num_ptr + 1, com_ptr + 1]
        
        return []