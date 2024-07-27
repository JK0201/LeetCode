class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = t = ListNode()
        cur_head = head
        cur_tail = head.next
        while cur_tail:
            n = gcd(cur_head.val, cur_tail.val)

            t.next = ListNode(val = cur_head.val)
            t = t.next
            t.next = ListNode(val = n)
            t = t.next

            cur_head, cur_tail = cur_head.next, cur_tail.next
        
        if cur_head:
            t.next = cur_head

        return h.next