class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        N= dummy
        h1=list1
        h2=list2
        while h1 and h2 :
            if h1.val>=h2.val:
                N.next=h2
                h2=h2.next
            else:
                N.next=h1
                h1=h1.next
            N=N.next
        N.next =h1 or h2
        return dummy.next
                