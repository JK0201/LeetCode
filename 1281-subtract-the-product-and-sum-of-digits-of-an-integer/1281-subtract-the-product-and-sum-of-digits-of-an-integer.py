class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mult_nums = 1
        sum_nums = 0
        for digit in str(n):
            mult_nums *= int(digit)
            sum_nums += int(digit)

        return mult_nums - sum_nums
