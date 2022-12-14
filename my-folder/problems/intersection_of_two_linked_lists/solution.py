# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # b = headB
        # a = headA
        # while a:
        #     b = headB
        #     while b:
        #         if b == a:
        #             return b
        #         else:
        #             b = b.next
        #     a = a.next
        # return None
        a = headA
        b = headB
        c1,c2=0,0
        while a:
            a = a.next
            c1+=1
        while b:
            b = b.next
            c2+=1
        print(c1,c2)
        d = abs(c1-c2)
        print(d)
        a = headA
        b = headB
        if c1>c2:
            for i in range(d):
                a = a.next
        else:
            for i in range(d):
                b = b.next
        print(a.val,b.val)
        while a and b:
            if a == b:
                return a
            a = a.next
            b = b.next
        return None
            
        
        