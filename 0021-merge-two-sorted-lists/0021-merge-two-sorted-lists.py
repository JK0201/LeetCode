class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                tail, list1 = tail.next, list1.next

            else:
                tail.next = list2
                tail, list2 = tail.next, list2.next

        if list1 or list2:
            tail.next = list1 if list1 else list2

        return head.next