from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    r = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self._subtree(root)
        return self.r

    def _subtree(self, root: TreeNode):
        if root.left != None:
            self._subtree(root.left)
        self.r.append(root.val)
        if root.right != None:
            self._subtree(root.right)