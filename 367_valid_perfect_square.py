# https://leetcode.com/problems/valid-perfect-square/

import math
class Solution:

    def highsquare(self):
        p = 1
        l = []
        while p < 10000:
            l.append(p*p)
            p += 1
        return l
    def isPerfectSquare(self, num: int) -> bool:
        c = int(math.sqrt(num))
        if c*c == num:
            return True
        else:
            return False


if __name__ == "__main__":
    inputs = [76, 16, 14, 9, 99980001, 5]
    inp = []
    S = Solution()
    for x in inputs:
        print(S.isPerfectSquare(x))

    # print(S.highsquare())