# https://leetcode.com/problems/arranging-coins/
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        calc1 = bool(math.sqrt(5 * (n**2) + 4) % 1 == 0)
        calc2 = bool(math.sqrt(5*(n**2)-4) % 1 == 0)

        if calc1 and calc2:
