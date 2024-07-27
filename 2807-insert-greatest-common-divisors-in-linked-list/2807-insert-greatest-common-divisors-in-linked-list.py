class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = t = ListNode()
        
        n = 0
        cur_head = head
        cur_tail = head.next
        while cur_tail:
            for i in range(1, min(cur_head.val, cur_tail.val) + 1):
                if cur_head.val % i == 0 and cur_tail.val % i == 0:
                    n = i

            t.next = ListNode(val = cur_head.val)
            t = t.next
            
            t.next = ListNode(val = n)
            t = t.next

            cur_head = cur_head.next
            cur_tail = cur_tail.next
        
        if cur_head:
            t.next = cur_head

        return h.next