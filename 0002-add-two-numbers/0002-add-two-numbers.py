# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        dummyNode=ListNode(-1)
        current=dummyNode
        t1=l1
        t2=l2
        carry=0
        while t1 or t2:
            sumi=carry
            if t1:sumi=sumi+t1.val
            if t2: sumi=sumi+t2.val
            current.next=ListNode(sumi % 10)
            carry=sumi//10
            current=current.next
            if t1: t1=t1.next
            if t2: t2=t2.next
        if carry:
            current.next=ListNode(carry)
        return dummyNode.next




        