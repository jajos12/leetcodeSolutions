class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        maxi = max(arr1)
        def checker(x, maxi):
            if x in arr2:
                return arr2.index(x)
            else:
                return x + maxi
        arr1.sort(key=lambda x: checker(x, maxi))
        return arr1