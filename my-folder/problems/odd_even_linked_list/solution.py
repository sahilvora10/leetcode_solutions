# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        o = head
        if head == None or head.next == None:
            return head
        e = head.next
        eh = head.next
        
        while e and e.next:
            o.next = o.next.next
            e.next = e.next.next
            o = o.next
            e = e.next
        o.next = eh
        return head
        