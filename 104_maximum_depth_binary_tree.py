from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    maxs = 0
    c = 0
    def maxDepth(self, root: TreeNode) -> int:
        self._maxDepth(root)
        return self.maxs
    def _maxDepth(self, root: TreeNode) -> None:



if __name__ == "__main__":
    T9 = TreeNode(val=9)
    T8 = TreeNode(val=8, right=T9)
    T7 = TreeNode(val=7, right=T8)
    T6 = TreeNode(val=6)
    T5 = TreeNode(val=5, left=T6, right=T7)
    T4 = TreeNode(val=4)
    T3 = TreeNode(val=3)
    T2 = TreeNode(val=2, left=T3, right=T4)
    T1 = TreeNode(val= 1, left=T2, right=T5)

    S = Solution()
    print(S.maxDepth(T1))





