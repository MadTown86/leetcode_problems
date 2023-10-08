# https://leetcode.com/problems/arranging-coins/
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:

        for x in range(n, -1, -1):
            calc1 = bool(math.sqrt(5 * (n ** 2) + 4) % 1 == 0)
            calc2 = bool(math.sqrt(5 * (n ** 2) - 4) % 1 == 0)
            print(f'{x=} :: {calc1=} :: {calc2=}')
            if calc1 and calc2:
                return x
            if calc1 or calc2:
                return x
            if x == 0:
                return 0
            if x == 1:
                return 1

if __name__ == "__main__":
    S = Solution()
    inp = [5, 10, 11, 15, 17]
    print(S.arrangeCoins(inp[0]))


