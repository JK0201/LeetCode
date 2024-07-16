class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        max = 0

        for n in nums:
            dict[n] = True
        
        for n in dict.keys():
            count = 1
            cur_num = n

            while cur_num + 1 in dict.keys():
                count += 1
                cur_num += 1
            
            if max < count:
                max = count
        
        return max