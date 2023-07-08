# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for x in nums1:
            if x in nums2 and x not in res:
                res += [x]*min([nums1.count(x), nums2.count(x)])
            else:
                continue
        return res

if __name__ == "__main__":
    inputs = [([1, 2, 2, 1], [2, 2]), ([5, 5, 5], [5, 5, 5, 5]), ([1, 1, 2, 3, 4], [2, 1])]
    S = Solution()
    for x, y in inputs:
        print(S.intersect(x, y))