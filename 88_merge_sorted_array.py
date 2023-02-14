"""
https://leetcode.com/problems/merge-sorted-array/
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_org = m
        while nums2:
            merge_val = nums2.pop(0)
            for x in range(0, m+1):
                if m == m_org + n:
                    nums1[m_org + n] = merge_val
                    break
                if nums1[x] < merge_val and x != m:
                    continue
                if nums1[x] < merge_val and x == m:
                    nums1[m] = merge_val
                    m += 1
                else:
                    for y in range(len(nums1)-1, x-1, -1):
                        nums1[y] = nums1[y-1]
                    nums1[x] = merge_val
                    m += 1
                    break



if __name__ == "__main__":
    nums1 = [1, 2, 4, 6, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    nums2 = [2, 3, 3, 5, 7, 8, 11, 13, 15, 17]
    m = 5
    n = 9
    S = Solution()
    S.merge(nums1, m, nums2, n)
    print(nums1)


