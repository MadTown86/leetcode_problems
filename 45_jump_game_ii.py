# https://leetcode.com/problems/jump-game-ii/description/
from typing import List
from functools import cache


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        crap = []

        @cache
        def f(i):
            if i == n - 1:
                return 0
            min_jumps = n - 1

            print(abs(n - (nums[i] + 1)))
            for j in (i + 1, i + nums[i]):
                jumps = f(j) + 1
                if jumps > 0:
                    min_jumps = min(min_jumps, jumps)
            return min_jumps

        # print(crap)
        return f(0)

    def jump2(self, nums: List[int]) -> int:
        i, j, n = 0, 1, len(nums)
        pass


if __name__ == "__main__":
    S = Solution()
    inputs = [[2, 3, 1, 1, 4], [2, 3, 0, 1, 4], [4, 1, 1, 1, 1]]

    for x in inputs:
        S.jump(x)
