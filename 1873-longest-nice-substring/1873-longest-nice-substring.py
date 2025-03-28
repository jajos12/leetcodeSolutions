class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(string):
            if len(string) < 2:
                return ""
            for i in range(len(string)):
                if string[i].swapcase() not in string:
                    left = helper(string[:i])
                    right = helper(string[i+1:])   
                    return left if len(left) >= len(right) else right
            return string
        return helper(s)