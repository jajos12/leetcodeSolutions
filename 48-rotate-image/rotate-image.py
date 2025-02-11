class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        j = 0
        for i in list(zip(*matrix[::-1])):
            matrix[j] = i
            j += 1