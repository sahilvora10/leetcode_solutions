# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        
        while a and b:
            if (a.val >= b.val):
                tail.next = b
                b = b.next
            else:
                tail.next = a
                a = a.next    
            tail = tail.next
        tail.next = a or b
        return (dummy.next)
        
        
        
        