class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        my_dict = defaultdict(list)
        answer = [0]*len(nums)
        freq = [0]*(max(nums)+1)
        for i in range(len(nums)):
            my_dict[nums[i]] += [i]
            freq[nums[i]] += 1
        smaller = 0
        # print(freq)
        for i in range(len(freq)):
            if freq[i] > 0:
                print(my_dict)
                for j in my_dict[i]:
                    answer[j] = smaller
                    print(smaller)
                smaller += freq[i]
        return answer