class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        def div(dividend, divisor):

            if dividend < divisor:
                return 0

            cur = divisor
            multiple = 1

            while cur + cur <dividend:  # 用加法求出保证divisor * multiple <= dividend的最大multiple
                cur += cur  # 即cur分别乘以1, 2, 4, 8, 16...2^n，即二进制搜索
                multiple += multiple

            return multiple + div(dividend - cur, divisor)

        if (divisor>=0 and dividend>=0) or (divisor<0 and dividend<0):


            if divisor < 0 and dividend < 0:
                divisor = -divisor
                dividend = -dividend

            res = div(dividend, divisor)
            return res

        else:
            if divisor<0:
                divisor=-divisor
            else:
                dividend=-dividend

            res = div(dividend, divisor)
            return -res



def rotate(matrix):
    n = len(matrix)
    # 沿着主对角线翻转
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print(matrix[0],'\n',matrix[1],'\n',matrix[2])
    # 每一行沿着中心列翻转
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
            print(matrix)


if __name__=='__main__':

    haystack = -2147483647
    needle = -1


    # print(Solution.divide(1,haystack,needle))


    left = len(s) - 1
    right = 0
    while left > right:
        List[left], List[right] = List[right], List[left]
        left -= 1
        right += 1
    return s


