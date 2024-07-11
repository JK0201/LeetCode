class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for cur_date, temp in enumerate(temperatures) :
            while stack and temp > stack[-1][1] :
                prev_date, _ = stack.pop()
                result[prev_date] = cur_date - prev_date
            stack.append((cur_date, temp))
        
        return result