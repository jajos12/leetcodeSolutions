class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        f_hash, n = defaultdict(int), len(fruits)
        max_fruit = float("-inf")
        left = 0
        for fruit in range(n):
            f_hash[fruits[fruit]] += 1
            while len(f_hash) > 2:
                f_hash[fruits[left]] -= 1
                if f_hash[fruits[left]] == 0:
                    del f_hash[fruits[left]]
                left += 1
            max_fruit = max(fruit-left+1, max_fruit)
        return max_fruit