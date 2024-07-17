class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        stack = [0] * 2 * len(nums)

        for i, n in enumerate(nums):
            stack[i] = n
            stack[i + len(nums)] = n 
        
        return stack