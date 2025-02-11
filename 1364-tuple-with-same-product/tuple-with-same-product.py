class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        my_dict = defaultdict(int)
        for i in nums:
            for j in nums:
                if i != j:
                    my_dict[i*j] += 1
                    # print(i, j)
        # print(my_dict, [j**2 - 2*j for i, j in my_dict.items() if j > 2])
        return sum([j**2 - 2*j for i, j in my_dict.items() if j > 2])