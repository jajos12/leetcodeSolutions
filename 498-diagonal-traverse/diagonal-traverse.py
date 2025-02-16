class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans, r, c = [], 0, 0
        d = 1 
        
        for _ in range(m*n):
            ans.append(mat[r][c])
            r, c = r-d, c+d

            if r<0 or r==m or c<0 or c==n:  
                if r==m: 
                    r=m-1
                    c+= -d + 1
                if c==n: 
                    c=n-1
                    r+= d + 1

                if r<0: r=0
                if c<0: c=0

                d = -d 
        return ans