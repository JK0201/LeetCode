class ListNode :
    def __init__(self, val = 0, next = None, prev = None) :
        self.val = val
        self.next = next
        self.prev = prev
        
class BrowserHistory : 
    def __init__(self, homepage) :
        self.head = self.tail = ListNode(val = homepage)

    def visit(self, url) :
        self.tail.next = ListNode(val = url, prev = self.tail)
        self.tail = self.tail.next

    def back(self, steps) :
        while steps > 0 and self.tail.prev != None :
            steps -= 1
            self.tail = self.tail.prev
        return self.tail.val

    def forward(self, steps) :
        while steps > 0 and self.tail.next != None :
            steps -= 1
            self.tail = self.tail.next
        return self.tail.val