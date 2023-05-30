# https://leetcode.com/problems/summary-ranges/
# *sigh*
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        x = 0
        y = 0
        for ind, x in enumerate(nums):
            if ind > 0 and nums[ind-1] != x-1:
                if x and y == 0:
                    res.append([0])





        return res

if __name__ == '__main__':
    inp1 = [0, 5, 6, 10, 11, 12, 15]
