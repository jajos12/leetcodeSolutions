# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        answer = []
        curr = head
        while curr:
            answer.append(curr.val)
            curr = curr.next
        return answer == answer[::-1]