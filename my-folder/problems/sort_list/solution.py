# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getmid(self,head):
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        return s
    
    def merge(self,left,right):
        tail = dummy = ListNode()
        while left and right:
            if left.val<right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        return dummy.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #merge sort
        #find the middle element
        if not head or not head.next:
            return head
        mid = self.getmid(head)
        # print(mid.val)
        l = head
        r = mid.next
        mid.next = None
        # print(l,r)
        l = self.sortList(l)
        r = self.sortList(r)
        return self.merge(l,r)
        
        