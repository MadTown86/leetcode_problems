# https://leetcode.com/problems/excel-sheet-column-number/
import string
caps = string.ascii_uppercase

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        s = ''.join(reversed(columnTitle))
        for x in range(len(columnTitle)):
            res += (ord(s[x])-64) * 26**x
        return res




"""
first A: 1-26
second A: 27-703
"""


if __name__ == "__main__":
    str1 = 'A'
    S = Solution()
    print(S.titleToNumber(str1))


"""
B = 2
C = 26*3
A = 26*26

B = 2 * 26**0
C = 3 + 26**1
B = 26*26*2 
"""