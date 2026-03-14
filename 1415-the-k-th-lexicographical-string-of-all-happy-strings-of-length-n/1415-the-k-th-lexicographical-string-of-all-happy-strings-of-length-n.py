class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        con = ['a', 'b', 'c']
        results = []
        
        def backtrack(current_str):
            if len(results) == k:
                return

            if len(current_str) == n:
                results.append(current_str)
                return
            
            for char in con:
                if not current_str or current_str[-1] != char:
                    backtrack(current_str + char)

        backtrack("")
        return results[k-1] if len(results) >= k else ""