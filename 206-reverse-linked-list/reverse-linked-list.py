# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        array = []
        curr = head
        while curr:
            array.append(curr.val)
            curr = curr.next
        i = len(array) - 1
        print(array, i)
        dummy = head
        while i>-1:
            dummy.val = array[i]
            dummy = dummy.next
            i -= 1
        return head