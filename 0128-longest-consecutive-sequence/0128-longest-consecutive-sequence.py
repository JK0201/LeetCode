class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = set(nums)
        longest = 0

        for n in dict:
            if n - 1 not in dict:
                count = 1
                next_num = n + 1

                while next_num in dict:
                    count += 1
                    next_num += 1
                longest = max(count, longest)

        return longest