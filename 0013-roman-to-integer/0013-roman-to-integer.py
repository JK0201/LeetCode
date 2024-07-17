class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }

        stack = []
        total = 0
        for r in s:
            if not stack:
                stack.append(r)

            elif (r == 'V' or r == 'X') and stack[-1] == 'I':
                total += dict[stack.pop() + r]

            elif (r == 'L' or r == 'C') and stack[-1] == 'X':
                total += dict[stack.pop() + r]

            elif (r == 'D' or r == 'M') and stack[-1] == 'C':
                total += dict[stack.pop() + r]

            else :
                stack.append(r)

        for r in stack:
            total += dict[r]

        return total


            