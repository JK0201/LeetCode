class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res = []

        heapq.heapify(nums)

        while nums:
            a = heapq.heappop(nums)
            alice = a
            b = heapq.heappop(nums)
            bob = b

            res.append(bob)
            res.append(alice)

        return res