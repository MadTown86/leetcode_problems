# https://leetcode.com/problems/pascals-triangle/
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        base = [[1], [1, 1]]
        if not numRows:
            return [[]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        elif numRows > 2:
            for x in range(2, numRows):
                add = [1]
                x = 0
                y = 1
                while y <= len(base[-1]):
                    print(f'Y: {y}')
                    add.append(base[-1][x] + base[-1][y])
                    if y == len(base[-1]) - 1:
                        add.append(base[-1][y])
                        break
                    x += 1
                    y += 1
                base.append(add)
        return base

if __name__ == "__main__":
    S = Solution()
    print(S.generate(8))