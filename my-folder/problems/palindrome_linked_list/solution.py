# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        t = head
        while (t!=None):
            stack.append(t.val)
            t = t.next
        print(stack)
        t = head
        while (t!=None):
            if t.val != stack.pop():
                return False
            t = t.next
        return True
            
            
        