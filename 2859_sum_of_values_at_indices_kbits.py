# https://leetcode.com/contest/weekly-contest-363/problems/sum-of-values-at-indices-with-k-set-bits/

from typing import List


class Solution:
    """
    Should have just stayed up for the weekly test.  At least would have gotten one answer.
    """

    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s = 0
        for x in range(len(nums)):
            if sum(int(x) for x in "{0:b}".format(x)) == k:
                s += nums[x]
        return s


if __name__ == "__main__":
    S = Solution()
    inp = [([5, 10, 1, 5, 2], 1), ([4, 3, 2, 1], 2)]

    assert S.sumIndicesWithKSetBits(*inp[0]) == 13
    assert S.sumIndicesWithKSetBits(*inp[1]) == 1
