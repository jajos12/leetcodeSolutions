class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solver(arr, pos):
            if len(arr) == 1:
                if pos%2:
                    return -arr[0]
                else:
                    return arr[0]
            if pos%2:
                return min(-arr[0]+solver(arr[1:], pos+1), -arr[-1]+solver(arr[:-1], pos+1))
            else:
                return max(arr[0]+solver(arr[1:], pos+1), arr[-1]+solver(arr[:-1], pos+1))
        # if len(nums) <= 1:
        #     return True
        max_c = solver(nums, 0)
        print(max_c)
        return max_c >= 0