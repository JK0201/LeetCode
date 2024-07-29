class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dict = {}
        res = []

        for i, s in enumerate(groupSizes):
            if s not in dict:
                dict[s] = [i]

            else:
                dict[s].append(i)

        for k, v in dict.items():
            if len(v) > k:
                i = 0
                while i < len(v):
                    res.append(v[i:i+k])
                    i += k

            else:
                res.append(v)

        return res