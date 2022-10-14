# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        s = head
        f = head
        prev = head
        while f!= None and f.next != None:
            prev = s
            s = s.next
            f = f.next.next
        prev.next = s.next
        return head
        
        