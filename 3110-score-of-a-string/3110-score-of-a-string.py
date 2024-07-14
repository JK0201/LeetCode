class Solution:
    def scoreOfString(self, s: str) -> int:
        stack = []
        total = 0

        for i in s:
            i = ord(i)
            
            if stack:
                total += abs(stack.pop() - i)
            stack.append(i)
        
        return total