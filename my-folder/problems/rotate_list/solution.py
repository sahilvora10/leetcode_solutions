# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or not head or not head.next:
            return head
        l = 0
        t = head
        while t:
            t = t.next
            l+=1
        if k%l==0:
            return head
        c = (l-k%l)
        t = head
        for i in range(c-1):
            t = t.next
        r = t.next
        t.next = None
        oh = head
        nh = r
        while r.next:
            r = r.next
        r.next = oh
        return nh
            
        