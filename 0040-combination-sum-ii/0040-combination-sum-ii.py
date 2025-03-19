class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def helper(temp, curr_sum, nxt):
            if curr_sum > target:
                return
            if curr_sum == target:
                result.append(temp[::])
                return
            else:
                i = nxt
                while i < len(candidates):
                    temp.append(candidates[i])
                    helper(temp, curr_sum+candidates[i], i+1)
                    temp.pop()
                    i += 1
                    while i  < len(candidates) and candidates[i] == candidates[i-1]:
                        i += 1
        helper([], 0, 0)
        return result