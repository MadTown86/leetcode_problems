# https://leetcode.com/problems/counting-bits/
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        print(str(bin(n), b))

if __name__ == "__main__":
    inputs = [1, 2, 3, 4, 5, 6]
    S = Solution()
    for x in inputs:
        S.countBits(x)