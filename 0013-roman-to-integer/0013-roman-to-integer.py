class Solution:
    def romanToInt(self, s: str) -> int:
        stack = []
        nums = []
        total = 0

        for r in s :
            if not stack :
                stack.append(r)

            else :
                if r == 'V' and stack[-1] == 'I' :
                    total += 4
                    stack.pop()

                elif r == 'X' and stack[-1] == 'I' :
                    total += 9
                    stack.pop()

                elif r == 'L' and stack[-1] == 'X' :
                    total += 40
                    stack.pop()

                elif r == 'C' and stack[-1] == 'X' :
                    total += 90
                    stack.pop()

                elif r == 'D' and stack[-1] == 'C' :
                    total += 400
                    stack.pop()

                elif r == 'M' and stack[-1] == 'C' :
                    total += 900
                    stack.pop()
                
                else :
                    stack.append(r)
                    
        for r in stack :
            if r == 'I' :
                total += 1
            
            elif r == 'V' :
                total += 5
            
            elif r == 'X' :
                total += 10

            elif r == 'L' :
                total += 50

            elif r == 'C' :
                total += 100

            elif r == 'D' :
                total += 500

            else :
                total += 1000

        return total

            