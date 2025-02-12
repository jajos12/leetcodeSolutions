class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        my_dict = defaultdict(list)
        maxim = 0
        max_len = 0
        nums.sort()
        for i in nums:
            sum_of_digit = sum(map(int, list(str(i))))
            my_dict[sum_of_digit].append(i)
            if max_len < len(my_dict[sum_of_digit]):
                max_len = len(my_dict[sum_of_digit])
            if maxim < sum(my_dict[sum_of_digit][-2:]) and len(my_dict[sum_of_digit]) > 1:
                maxim = sum(my_dict[sum_of_digit][-2:])

        print(my_dict, max_len)
        return maxim if max_len > 1 else -1