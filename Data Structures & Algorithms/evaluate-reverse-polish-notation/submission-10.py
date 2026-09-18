class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if t == "+":
                    stack.append(num1 + num2)
                elif t == "-":
                    stack.append(num1 - num2)
                elif t == "*":
                    stack.append(num1 * num2)
                else:
                    result = num1 / num2
                    if result < 0:
                        result = math.ceil(result)
                    else:
                        result = math.floor(result)
                    stack.append(int(result))
        return stack.pop()
