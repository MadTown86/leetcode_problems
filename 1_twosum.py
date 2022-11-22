"""
https://leetcode.com/problems/two-sum/?envType=study-plan&id=data-structure-i
"""

# Question didn't specify whether you could sort the list
class Solution:
    # If you can find it in one pass, great, otherwise accumulate lower values to separate list
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        newnums = sorted(enumerate(nums))
        i, j = 0, len(newnums)-1
        while newnums

if __name__ == "__main__":
    S = Solution()
    testcase = ([2, 4, 21, 33, 2, 16, 6, 13, 1, 1, 11, 5], 16)
    testcase2 = ([5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5], 10)
    testcase3 = ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1)
    testcase4 = ([0, 4, 3, 0], 0)
    print(S.twoSum(*testcase4))