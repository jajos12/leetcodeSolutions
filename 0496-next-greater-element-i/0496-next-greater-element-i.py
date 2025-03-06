class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        answer = defaultdict(int)
        for i in range(len(nums2)-1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()

            if stack:
                answer[nums2[i]] = stack[-1]
            else:
                answer[nums2[i]] = -1
            stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i] = answer[nums1[i]]
        return nums1