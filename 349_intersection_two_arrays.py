# https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List
from itertools import zip_longest
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for x in nums1:
            if x in nums2 and x not in res:
                res.append(x)
            else:
                continue
        return res

if __name__ == "__main__":
    inputs = [([1, 2, 2, 1], [1, 4, 2, 2]), ([1, 1, 1], [1, 1, 1]), ([0, 0, 0], [1, 1, 1]), ([1, 2, 3], [5, 7, 9, 1, 2, 3])]
    S = Solution()
    for x, y in inputs:
        print(S.intersection(x, y))

