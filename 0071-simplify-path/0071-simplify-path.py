class Solution:
    def simplifyPath(self, path: str) -> str:
        splitted = path.split("/")
        stack = []
        print(splitted)
        for i in splitted:
            if i == ".." and len(stack):
                stack.pop()
            elif i != "." and i != "" and i != "..":
                stack.append(i)
        return '/' + "/".join(stack)