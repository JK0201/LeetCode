class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = sorted(nums)
        left = 0
        right = len(list) - 1
        result = []
        
        while left < right :
            total = list[left] + list[right]
            
            if total < target :
                left += 1
            
            elif total > target :
                right -= 1
                
            else :
                break
            
        for n in range(len(nums)) :
            if nums[n] == list[left] or nums[n] == list[right] :
                result.append(n)
                
        result.sort()
        return result
        