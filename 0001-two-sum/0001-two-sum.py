class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.list = sorted(nums)
        self.left = 0
        self.right = len(self.list) - 1
        result = []
        
        while self.left < self.right :
            total = self.list[self.left] + self.list[self.right]
            if total < target :
                self.left += 1
            elif total > target :
                self.right -= 1
            else :
                break
        
        for i in range(len(nums)) :
            if nums[i] == self.list[self.left] :
                result.append(i)
            elif nums[i] == self.list[self.right] :
                result.append(i)
        
        result.sort()
        return result
        