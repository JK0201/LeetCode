class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i+1 for i in range(n)]
        res = ''
        cnt = 0

        def backtrack(curr):
            nonlocal cnt, res

            if len(curr) == n:
                cnt += 1
                if cnt == k:
                    res = ''.join(map(str, curr))
                    raise StopIteration
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
        try:
            backtrack([])
        except StopIteration:
            pass
            
        return res