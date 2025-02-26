class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxim = float("-inf")
        minim = float("inf")
        run_sum = 0
        run_sum1 = 0
        for i in nums:
            if run_sum+i > 0:
                run_sum = 0
                run_sum1 += i
            elif run_sum1+i < 0:
                run_sum1 = 0
                run_sum += i
            else:
                run_sum1+=i
                run_sum+=i
                
            minim = min(minim, run_sum)
            maxim = max(maxim, run_sum1)
        return max(abs(minim), maxim)
            
            