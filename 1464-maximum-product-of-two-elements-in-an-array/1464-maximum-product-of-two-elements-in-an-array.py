import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [i * -1 for i in nums]
        heapq.heapify(nums)

        m = heapq.heappop(nums) * -1
        n = heapq.heappop(nums) * -1

        return (m-1) * (n-1)