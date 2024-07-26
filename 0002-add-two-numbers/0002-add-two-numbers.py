class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        calc = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        total = [int(i) for i in calc]

        head = tail = ListNode(val = total[0])
        i = 1

        while i < len(total):
            tail.next = ListNode(val = total[i])
            tail = tail.next
            i += 1

        return head