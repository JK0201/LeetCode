class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        dict = {}

        for i, s in enumerate(stones):
            if s not in dict:
                dict[s] = 1
            else:
                dict[s] += 1

        for j in jewels:
            if j in dict:
                cnt += dict[j]

        return cnt