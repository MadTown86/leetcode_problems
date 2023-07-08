# https://leetcode.com/problems/counting-bits/
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [x for x in [sum([int(y) for y in format(b, '010b')]) for b in range(n+1)]] if n > 0 else [0]


if __name__ == "__main__":
    inputs = [1, 2, 3, 4, 5, 6]
    S = Solution()
    for x in inputs:
        print(S.countBits(x))