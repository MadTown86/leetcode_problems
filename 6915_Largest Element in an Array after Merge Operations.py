#  https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

from typing import List
from itertools import groupby

class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        trail = len(nums)-1
        lead = trail - 1
        while lead >= 0:
            if nums[lead] <= nums[trail]:
                nums[lead] = nums[lead] + nums.pop(trail)
                trail = lead
                lead = trail - 1
            else:
                trail = lead
                lead = trail - 1
        print(nums)

if __name__ == "__main__":
    S = Solution()
    inputs = [[2,3,7,9,3], [5,3,3]]

    """
    - Choose i = 0. The resulting array will be nums = [5,7,9,3].
    - Choose i = 1. The resulting array will be nums = [5,16,3].
    - Choose i = 0. The resulting array will be nums = [21,3].
    """

    for x in inputs:
        print(S.maxArrayValue(x))




