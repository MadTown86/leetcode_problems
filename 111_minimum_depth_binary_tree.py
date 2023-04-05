from typing import Tuple, Any

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left and not root.right:
            return self.minDepth(root.left) + 1
        else:
            return self.minDepth(root.right) + 1


if __name__ == '__main__':
    N1 = TreeNode(1)
    N2 = TreeNode(2)
    N3 = TreeNode(3)
    N4 = TreeNode(4)
    N5 = TreeNode(5)

    N1.left = N2
    N2.left = N3
    N3.left = N4
    N1.right = N5

    L1 = TreeNode(2)
    L3 = TreeNode(3)
    L5 = TreeNode(4)
    L6 = TreeNode(5)
    L8 = TreeNode(6)
    L1.right = L3
    L3.right = L5
    L5.right = L6
    L6.right = L8

    S = Solution()
    print(S.minDepth(L1))