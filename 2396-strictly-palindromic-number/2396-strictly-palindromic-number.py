class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-2+1):
            num = n
            s = ''

            while num > 0:
                num, mod = divmod(num, i)
                s += str(mod)

            if s != s[::-1]:
                return False
        
        return True