"""
https://leetcode.com/problems/merge-sorted-array/
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for x in range(m + n):
            print(x)
            print(nums1)
            zero_ind = m + x + 1
            nums2_val = nums2.pop(0)
            if nums1[x] < nums2_val:
                for y in range(zero_ind, x, -1):
                     nums1[y] = nums1[y-1]
                nums1[x + 1] = nums2_val




if __name__ == "__main__":
    nums1 = [1, 2, 4, 6, 0, 0, 0, 0]
    nums2 = [3, 5, 6, 8]
    m = 4
    n = 4
    S = Solution()
    S.merge(nums1, m, nums2, n)
    print(nums1)


