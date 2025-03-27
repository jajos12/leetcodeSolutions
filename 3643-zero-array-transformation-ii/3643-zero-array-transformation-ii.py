class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left, right = 0, len(queries)
        sth = False
        while left <= right:
            mid = (left+right)//2
            diff = [0]*(len(nums)+1)
            for i in range(mid):
                diff[queries[i][0]] -= queries[i][2]
                diff[queries[i][1]+1] += queries[i][2]
            diff = list(accumulate(diff))
            possible = False
            for i, j in zip(diff, nums):
                if j + i > 0:
                    break
            else:
                possible = True
                sth = True
            if possible:
                right = mid-1
            else:
                left = mid+1
            # print(diff, mid)
        return right+1 if sth else -1