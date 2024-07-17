class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {n : n + 1 for n in nums}
        longest = 0

        for n in dict:
            if n - 1 not in dict:
                count = 1
                target = dict[n]

                while target in dict:
                    count += 1
                    target += 1
                longest = max(count, longest)

        return longest