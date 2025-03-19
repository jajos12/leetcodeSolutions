class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def helper(temp, count, nxt):
            if count == k:
                result.append(temp[:])
                return
            else:
                for i in range(nxt, n+1):
                    temp.append(i)
                    helper(temp, count+1, i+1)
                    temp.pop()
        helper([], 0, 1)
        return result