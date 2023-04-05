# https://leetcode.com/problems/pascals-triangle-ii/
from typing import List
import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for x in range(0, rowIndex+1):
            adds = math.factorial(rowIndex) // (math.factorial(rowIndex-x) * math.factorial(x))
            res.append(adds)

        return res

if __name__ == '__main__':
    S = Solution()
    print(S.getRow(1))