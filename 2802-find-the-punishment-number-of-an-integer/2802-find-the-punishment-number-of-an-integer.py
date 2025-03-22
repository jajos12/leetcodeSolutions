class Solution:
    def punishmentNumber(self, n: int) -> int:
        self.ans = 0
        def backtrack(num, indx, k):
            if indx == len(num):
                return k == 0
            for i in range(indx, len(num)):
                curr = int(num[indx:i+1])
                if backtrack(num, i+1, k-curr):
                    return True
            return False

        for i in range(1, n+1):
            if backtrack(str(i*i), 0, i):
                self.ans += i*i
        return self.ans