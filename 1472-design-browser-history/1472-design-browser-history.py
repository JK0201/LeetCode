class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        self.idx += 1
        self.history.insert(self.idx, url)

        for _ in range(self.idx + 1, len(self.history)):
            self.history.pop()
        
    def back(self, steps: int) -> str:
        self.idx -= steps
        if self.idx < 0:
            self.idx = 0
        return self.history[self.idx]
        

    def forward(self, steps: int) -> str:
        self.idx += steps
        if self.idx > len(self.history) - 1:
            self.idx = len(self.history) - 1
        return self.history[self.idx]