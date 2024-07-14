class NodeList:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.tail = NodeList(val = homepage)

    def visit(self, url: str) -> None:
        self.tail.next = NodeList(val = url, prev = self.tail)
        self.tail = self.tail.next        
        return None

    def back(self, steps: int) -> str:
        while steps > 0 and self.tail.prev != None:
            self.tail = self.tail.prev
            steps -= 1
        return self.tail.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.tail.next != None:
            self.tail = self.tail.next
            steps -= 1
        return self.tail.val