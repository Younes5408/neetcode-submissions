class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        N = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                N.next = list1
                list1 = list1.next
            else:
                N.next = list2
                list2 = list2.next
            N = N.next
        N.next = list1 or list2
        return dummy.next