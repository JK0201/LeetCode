# Definition for singly-linked list.
class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, val = 0):
        self.head = self.tail = Node(val = val)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        li = []

        cur_node = list1
        while cur_node:
            li.append(cur_node.val)
            cur_node = cur_node.next

        cur_node = list2
        while cur_node:
            li.append(cur_node.val)
            cur_node = cur_node.next

        li.sort()
        node = LinkedList(li[0])

        cur_node = node.tail
        for i in range(1, len(li)):
            cur_node.next = Node(li[i])
            cur_node = cur_node.next

        return node.head