class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in s:
            if i == "#" and len(stack1):
                stack1.pop()
            elif i != "#":
                stack1.append(i)
        for i in t:
            if i == "#" and len(stack2):
                stack2.pop()
            elif i != "#":
                stack2.append(i)
        print(stack1, stack2)
        return stack1 == stack2