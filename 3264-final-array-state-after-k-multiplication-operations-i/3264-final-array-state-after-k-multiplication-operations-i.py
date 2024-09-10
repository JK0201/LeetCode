import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(pq)

        while k > 0:
            minNum, order = heapq.heappop(pq)
            heapq.heappush(pq, (minNum * multiplier, order))
            k -= 1

        return [i[0] for i in sorted(pq, key = lambda x : x[1])]
        