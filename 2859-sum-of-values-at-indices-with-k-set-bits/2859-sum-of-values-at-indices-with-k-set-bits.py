class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total = 0
        for i, n in enumerate(nums):
            target = str(bin(i)[2:])
            if target.count('1') == k:
                total += n

        return total