# https://leetcode.com/problems/valid-perfect-square/

import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        try:
            p = math.log(num) / math.log(2)
            print(p)
            if p % 1 == 0:
                return True
            else:
                return False
        except:
            return False

if __name__ == "__main__":
    inputs = [16, 14, 9]
    S = Solution()
    for x in inputs:
        print(S.isPerfectSquare(x))