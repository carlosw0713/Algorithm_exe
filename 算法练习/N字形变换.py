


s='PAYPALISHIRING'
# print(x[2])

# 0 (n-1)*2 (n-1)*4
# 1 (n-1)*2-1

n=3



class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1: return s #当只有一位数时

        rows = [""] * numRows
        print(rows)
        n = 2 * numRows - 2 #通过倍数取余判断在那一行
        for i, char in enumerate(s):
            x = i % n

            # min(x,n-x) 取最小那边的余 防止7%4=3 应该为1

            rows[min(x, n - x)] += char
        return "".join(rows)




print(Solution.convert(1,s,3))
print('PAHNAPLSIIGYIR')


'''0,4
06'''
