from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = deque()
        if x < 0 :
            return False
        
        else :
            for i in str(x) :
                nums.append(i)
            
            while len(nums) > 1 :
                if nums.popleft() != nums.pop() :
                    return False
                
        return True   