# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = head.val
        head = head.next
        while head:
            n = n<<1
            n+=head.val
            head = head.next
        return n
        