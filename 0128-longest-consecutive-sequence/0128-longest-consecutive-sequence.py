class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        max = 0

        for n in nums:
            dict[n] = 0

        for n in dict.keys():
            if n - 1 not in dict.keys():
                count = 0
                cur_num = n
                
                while cur_num in dict.keys():
                    count += 1
                    cur_num += 1

                if max < count:
                    max = count


        return max