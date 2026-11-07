class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        h= dummy
        l1,l2= list1,list2
        while l1 and l2:
            if l1.val >= l2.val:
                h.next = l2
                l2=l2.next
            else:
                h.next = l1
                l1= l1.next
            h= h.next
        h.next= l1 or l2
        
        return dummy.next
            

