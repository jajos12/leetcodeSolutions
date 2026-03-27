class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        idx = k % len(mat[0])
        for lst in mat:
            if lst[idx:] + lst[:idx] != lst:
                return False
        return True