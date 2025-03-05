class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_d = {')': '(', "]": "[", "}": "{"}
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if len(stack) and my_d[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
            