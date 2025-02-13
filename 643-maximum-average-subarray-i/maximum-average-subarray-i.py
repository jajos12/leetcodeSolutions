class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cont_sum = sum(nums[:k])
        # print(cont_sum)
        max_avg = cont_sum/k    
        prev = 0
        for i in range(1, len(nums) - k+1):
            cont_sum += nums[i+k-1] - nums[prev] 
            # print(max_avg, cont_sum, i+k)
            prev += 1
            if max_avg < cont_sum/k:
                max_avg = cont_sum/k
        return max_avg