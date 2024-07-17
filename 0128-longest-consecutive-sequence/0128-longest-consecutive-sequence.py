class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest = 1
        count = 1

        for i in range(len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    count += 1

                else:
                    longest = max(count, longest)
                    count = 1

        return max(count, longest)