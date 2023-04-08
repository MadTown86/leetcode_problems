# https://leetcode.com/problems/majority-element/

from typing import List

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        C = Counter(nums)
        return C.most_common(1)[0][0]


if __name__ == '__main__':
    nums = [2, 2, 2, 1, 1, 3]
    S = Solution()
    print(S.majorityElement(nums))