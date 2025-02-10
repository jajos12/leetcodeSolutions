class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([x[0] * x[1] for x in sorted(list(Counter(s).items()), key=lambda x: x[1], reverse=True)])