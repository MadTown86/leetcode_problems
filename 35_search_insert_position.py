class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        def recurse_inner(target, left, right):
            if right - left < 3:
                pos = left if nums[left] >= target else right
                return pos
            else:
                pos = nums[left:right]