class Solution:
    def paly(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        counter = 0
        while left <= right:
            print("left is", left, s[left], "right is", right, s[right])
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.paly(s, left + 1, right) or self.paly(s,left, right-1)
        return True