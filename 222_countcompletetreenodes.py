# https://leetcode.com/problems/count-complete-tree-nodes/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        left = root.left
        right = root.right

        counter = 0
        while left.left and right.right:
            left.left = left.left.left
            right.right = right.right.right
