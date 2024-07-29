from collections import deque

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        nums1 = deque(nums[0:n])
        nums2 = deque(nums[n:])

        while nums1 and nums2:
            res.append(nums1.popleft())
            res.append(nums2.popleft())

        if nums1 or nums2:
            res.append(nums1 if nums1 else nums2)

        return res