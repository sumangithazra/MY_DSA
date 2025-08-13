# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return True
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        current=slow
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        first_half=head
        second_half=prev
        while second_half:
            if first_half.val!=second_half.val:
                return False
            first_half=first_half.next
            second_half=second_half.next
        return True
        