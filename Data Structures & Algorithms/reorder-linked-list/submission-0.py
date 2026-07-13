# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f=head,head.next
        while f and f.next:
            s=s.next
            f=f.next.next
        second=s.next
        prev=s.next= None
        while second :
            tmp=second.next 
            second.next=prev
            prev=second
            second=tmp
        un , deux = head, prev
        while deux :
            tmp1,tmp2=un.next ,deux.next
            un.next=deux
            deux.next=tmp1
            un , deux = tmp1, tmp2
            