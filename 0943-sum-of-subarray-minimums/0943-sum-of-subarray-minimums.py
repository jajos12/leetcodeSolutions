from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0
        n = len(arr)
        
        prev_smaller = [-1] * n
        next_smaller = [n] * n
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()  
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                next_smaller[stack.pop()] = i
            stack.append(i)

        for i in range(n):
            left_count = i - prev_smaller[i]
            right_count = next_smaller[i] - i  
            result = (result + arr[i] * left_count * right_count) % MOD
        
        return result
