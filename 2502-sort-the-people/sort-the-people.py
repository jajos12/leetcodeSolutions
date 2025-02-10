class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # insertion sort
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if heights[j] > heights[i]:
                    heights.insert(i, heights[j])
                    heights.pop(j+1)
                    names.insert(i, names[j])
                    names.pop(j+1)
                    # names[i], names[j] = names[j], names[i]
        return names

                    