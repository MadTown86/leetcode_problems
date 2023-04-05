# https://leetcode.com/problems/majority-element/

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        C = Counter(nums)
        return C.most_common(1)[0][0]