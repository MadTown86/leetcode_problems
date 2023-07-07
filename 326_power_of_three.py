# https://leetcode.com/problems/power-of-three/
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        try:
            p = math.log10(n) / math.log10(3)
        except:
            return False
        return p % 1 == 0

if __name__ == "__main__":
    args = [8, 27, 9, -1]
    S = Solution()
    for x in args:
        print(S.isPowerOfThree(x))
