class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        idx = 0
        
        for t in temperatures :
            while stack and t > stack[-1][1] :
                target = stack.pop()
                date = idx - target[0]
                result[target[0]] = date
            stack.append([idx, t])
            idx += 1
        
        return result
                