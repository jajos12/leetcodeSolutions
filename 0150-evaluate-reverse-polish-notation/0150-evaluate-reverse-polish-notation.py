class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        answer = None
        for i in tokens:
            try:
                stack.append(float(i))
            except ValueError:
                if len(stack) > 1:
                    assign = eval(f"{stack[-2]}{i}{stack[-1]}")
                    assign = assign.__ceil__() if assign < 0 else assign.__floor__()
                    stack.pop()
                    stack.pop()
                    stack.append(assign)
        return int(stack[0])