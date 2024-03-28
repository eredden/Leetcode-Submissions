# https://leetcode.com/submissions/detail/1215529284/

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack  = []
        answer = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                answer[stack_index] = index - stack_index

            stack.append([temp, index])

        return answer