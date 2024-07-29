class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        t = n

        while True:
            if t % n == 0 and t % 2 == 0:
                return t
            t += 1