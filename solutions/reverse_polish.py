# https://leetcode.com/submissions/detail/1212698714/

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                # second operand popped from stack first
                # to prevent ordering issues with operations
                operand = stack.pop()

                if token == "+":
                    stack.append(int(stack.pop() + operand))
                elif token == "-":
                    stack.append(int(stack.pop() - operand))
                elif token == "*":
                    stack.append(int(stack.pop() * operand))
                elif token == "/":
                    stack.append(int(stack.pop() / operand))
            else:
                stack.append(int(token))
        
        return stack[0]