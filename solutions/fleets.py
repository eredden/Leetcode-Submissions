# https://leetcode.com/problems/car-fleet/submissions/1217597855/

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in pairs:
            stack.append((target - p) / s)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)