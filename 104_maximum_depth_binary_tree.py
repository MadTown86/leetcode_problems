from collections import deque
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
        if not root.left and not root.right:
            if self.c > self.maxs:
                self.maxs = self.c
                self.c = 0
        if root.left:
            self.c += 1
            self._maxDepth(root.left)
        if root.right:
            self.c += 1
            self._maxDepth(root.right)

if __name__ == "__main__":

    T8 = TreeNode()
    T7 = TreeNode(right=T8)
    T6 = TreeNode()
    T5 = TreeNode(left=T6, right=T7)
    T4 = TreeNode()
    T3 = TreeNode()
    T2 = TreeNode(left=T3, right=T4)
    T1 = TreeNode(left=T2, right=T5)

    S = Solution()
    print(S.maxDepth(T1))





