# https://leetcode.com/submissions/detail/1213595375/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        result = []

        def backtrack(open_number: int, closed_number: int):
            if open_number == closed_number == n:
                result.append("".join(stack))
                return

            if open_number < n:
                stack.append("(")
                backtrack(open_number + 1, closed_number)
                stack.pop()

            if closed_number < open_number:
                stack.append(")")
                backtrack(open_number, closed_number + 1)
                stack.pop()

        backtrack(0, 0)

        return result