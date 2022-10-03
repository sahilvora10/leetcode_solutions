# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = ListNode()
        res = n
        s = 0
        head = head.next
        while head:
            if head.val == 0:
                n.next = ListNode(s)
                s =0
                n = n.next
            s += head.val
            head = head.next
        return res.next
        