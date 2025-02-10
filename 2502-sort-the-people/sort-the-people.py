class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            swapped = 0
            for h in range(len(heights)-i-1):
                if heights[h] < heights[h+1]:
                    heights[h], heights[h+1] = heights[h+1], heights[h]
                    names[h], names[h+1] = names[h+1], names[h]         
                else:
                    swapped += 1
            if swapped == len(names):
                return names
        return names