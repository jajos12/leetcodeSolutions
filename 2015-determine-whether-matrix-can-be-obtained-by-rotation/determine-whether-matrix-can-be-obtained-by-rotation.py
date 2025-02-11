class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rows, cols = len(mat), len(mat[0])
        answer = False
        j = 0
        for _ in range(4):
            for i in list(zip(*mat[::-1])):
                print(j)
                mat[j] = i
                j += 1
            j = 0
            answer |= target == list(map(lambda i: list(i), mat))
        return answer