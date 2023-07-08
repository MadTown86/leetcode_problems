# https://leetcode.com/problems/power-of-four/

import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        try:
            p = math.log(n) / math.log(4)
            return p % 1 == 0
        except:
            return False

if __name__ == "__main__":
    inputs = [0, -1, -16, 16, 64, 1, 5]
    S = Solution()
    for arg in inputs:
        print(S.isPowerOfFour(arg))

