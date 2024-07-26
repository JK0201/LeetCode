class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        for n in nums:
            if n % 3 == 0:
                pass

            elif (n - 1) % 3 == 0 or (n + 1) % 3 == 0:
                cnt += 1

        return cnt