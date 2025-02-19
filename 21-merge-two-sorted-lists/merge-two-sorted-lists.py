# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        dummy = newList
        dummy1 = list1
        dummy2 = list2
        while dummy1 and dummy2:
            maxim = min(dummy1.val, dummy2.val)
            print(dummy, dummy1, dummy2, maxim)
            new = ListNode(maxim)
            if dummy1.val <= dummy2.val:
                dummy.next = new
                dummy = dummy.next
                dummy1 = dummy1.next
            else:
                dummy.next = new
                dummy = dummy.next
                dummy2 = dummy2.next
        if dummy1:
            dummy.next = dummy1        
        elif dummy2:
            dummy.next = dummy2
        return newList.next