class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dict = {}

        for n in nums:
            if n not in dict:
                dict[n] = 1

            else:
                dict[n] += 1

        res = []
        grp = []
        while True:
            for k in dict:
                if dict[k] != 0:
                    dict[k] -= 1
                    grp.append(k)

            if not grp:
                break
            
            res.append(grp)
            grp = []

        return res