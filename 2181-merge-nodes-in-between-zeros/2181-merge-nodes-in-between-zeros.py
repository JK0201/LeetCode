class Solution:
    def mergeNodes(self, list: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = ListNode()
        cur_node = list.next
        total = 0

        while cur_node:
            if cur_node.val == 0:
                tail.next = ListNode(total)
                tail = tail.next
                total = 0

            else:
                total += cur_node.val

            cur_node = cur_node.next
            
        return head.next