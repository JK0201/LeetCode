class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        stack = []

        for c in command:
            if c == '(':
                stack.append(')')

            elif c == ')' and stack[-1] == c:
                stack.pop()
                stack.append('o')
                res += 'o'

            elif c == 'a' and stack[-1] == ')':
                stack.pop()
                stack.append(c)
                res += c

            elif c == ')' and stack[-1] == 'l':
                pass

            else:
                stack.append(c)
                res += c

        return res