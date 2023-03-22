class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left:
            return self.minDepth()


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

    S = Solution()
    print(S.minDepth(N1))