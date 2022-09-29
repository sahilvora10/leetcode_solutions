# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        # head.next = None
        t = head
        c = 0
        while l1 or l2 or c>0:
            s = 0
            if l1:
                s += l1.val
                l1=l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            if c>0:
                s += c
            r = s//10
            s = s%10
            c = r
            print(s,r)
            t.next = ListNode(s)
            t = t.next
        return head.next
            
        