class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def solver(temp, start, close):
            if start == n and close == n:
                result.append(temp)
                return
            if start < n:
                solver(temp+"(", start+1, close)
            
            if close < start:
                solver(temp+")", start, close+1)
            
        solver("", 0, 0)
        return result