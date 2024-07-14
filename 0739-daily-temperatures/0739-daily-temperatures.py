class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for cur_date, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prev_date = stack.pop()[0]
                date = cur_date - prev_date
                result[prev_date] = date
            stack.append((cur_date, temp))

        return result