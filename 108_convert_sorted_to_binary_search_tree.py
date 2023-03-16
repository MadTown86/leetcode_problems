# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums and len(nums) > 1:
            prev = TreeNode(nums.pop())
            cursor = TreeNode(nums.pop())
        primrose = TreeNode(nums[0])