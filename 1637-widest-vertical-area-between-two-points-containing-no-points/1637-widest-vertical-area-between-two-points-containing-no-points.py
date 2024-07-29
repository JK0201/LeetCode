class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        l = 0
        r = 1
        max_length = 0

        while r < len(points):
            x1 = points[l][0]
            x2 = points[r][0]

            length = x2 - x1
            max_length = max(length, max_length)

            l += 1
            r += 1

        return max_length