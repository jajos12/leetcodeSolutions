class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # counting sort
        freq = [0 for i in range(max(heights)+1)]
        my_dict = defaultdict(str)
        for i in range(len(heights)):
            freq[heights[i]] += 1
            my_dict[heights[i]] = names[i]
        curr = 0
        for i in range(len(freq)-1, -1, -1):
            if freq[i] != 0:
                names[curr] = my_dict[i]
                curr += 1
        return names