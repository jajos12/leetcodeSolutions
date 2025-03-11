class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [0]*(rowIndex+1)
        for i in range(rowIndex+1):
            answer[i] = math.comb(rowIndex, i)
        return answer