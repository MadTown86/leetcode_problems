# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        if not root:
            return []
        return []

"""
Got it first time:  Lol, guess I have fiddled with this enough now to have some of it commit to memory

Other answers below:



"""