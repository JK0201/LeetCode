class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0
        dict = {c : i for i, c in enumerate(s)}

        for i in range(len(t)):
            cur = t[i]
            if cur in dict:
                res += abs(dict[cur] - i)
        
        return res