class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # 0
        # 0 1 1
        # 0 1 1 
        def solver(string, reverse, n):
            if n == 1:
                return string
            mod_str = string+"1"+reverse
            mod_rev = string+"0"+reverse
            return solver(mod_str, mod_rev, n-1)
        string = "0"
        reverse = "1"
        return solver(string, reverse, n)[k-1]