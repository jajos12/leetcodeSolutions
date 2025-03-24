import re
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def solver(temp, indx, cnt):
            if cnt == 4:
                if indx == len(s):
                    res.append(".".join(temp))
                return
            for i in range(indx, len(s)):
                if s[indx] == "0" and indx < i:
                    continue
                if int(s[indx:i+1]) < 256:
                    temp.append(s[indx:i+1])
                    solver(temp, i+1, cnt+1)
                    temp.pop()
                else:
                    return
        solver([], 0, 0)
        return res