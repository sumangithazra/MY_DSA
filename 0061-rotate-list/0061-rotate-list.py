# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None: return head
        count=1
        temp=head

        while temp.next:
            count+=1
            temp=temp.next
        k=k % count
        temp.next=head
        #temp=head
        remain=count-k
        while remain:
            remain-=1
            temp=temp.next
        head=temp.next
        temp.next=None
        return head
    
        