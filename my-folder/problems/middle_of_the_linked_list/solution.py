# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head
        f = head
        while (f):
            f = f.next
            if f:
                f = f.next
            else:
                break
            s = s.next
        return s
        