# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a,dummy= head , ListNode(0, head)
        b=dummy
        while n>0:
            a=a.next
            n-=1
        while a :
            b=b.next
            a=a.next
        b.next=b.next.next
        return dummy.next