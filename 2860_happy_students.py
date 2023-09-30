# https://leetcode.com/contest/weekly-contest-363/problems/happy-students/

from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        """
        Trying to wrap my head around the different ways to select:

        Looked up the answer.
        """
        nums += [float("-inf"), float("inf")]
        nums.sort()

        cnt = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < i - 1 < nums[i]:
                cnt += 1
        return cnt


if __name__ == "__main__":
    S = Solution()
    inp = [[1, 1], [0, 2, 3, 3, 6, 6, 7, 7], [1, 1, 4, 5, 10, 12]]
    assert S.countWays(inp[0]) == 2
    assert S.countWays(inp[1]) == 3
    assert S.countWays(inp[2]) == 2
