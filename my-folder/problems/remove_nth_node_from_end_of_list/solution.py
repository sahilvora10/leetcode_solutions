# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp  = head
        slow = head
        for i in range(n):
            temp = temp.next
        if temp == None:
            return head.next
        while temp.next != None:
            slow = slow.next
            temp = temp.next
        slow.next = slow.next.next
        return head
            
        
#         temp = head
#         l = 0
        
#         while temp != None:
#             l += 1
#             temp = temp.next
        
#         temp = head
        
#         if l == n:
#             head  = head.next
#             return head
#         c = 0
#         while c < l - n-1 and temp!=None:
#             temp = temp.next
#             c += 1
        
            
#         if temp.next:
#             temp.next = temp.next.next
#         else:
#             return None
#         return head
          


        
        