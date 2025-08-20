# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current=head
        prv=None
        while current:
            if current.val==val:
                if prv is None:
                    head=current.next
                else:
                    prv.next=current.next
                current=current.next
            else:
                prv=current
                current=current.next
        return head


        
        