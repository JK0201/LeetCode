class BrowserHistory:
    def __init__(self, homepage):
        self.list = [ homepage ]
        self.idx = 0
        
    def visit(self, url):
        self.idx += 1
        self.list.insert(self.idx, url) 
        for _ in range(self.idx + 1, len(self.list)) :
            self.list.pop()
        return None
        
    def back(self, steps) :
        self.idx -= steps
        if self.idx < 0 :
            self.idx = 0
        return self.list[self.idx]
    
    def forward(self, steps) :
        self.idx += steps
        if self.idx > len(self.list) - 1 :
            self.idx = len(self.list) - 1
        return self.list[self.idx]