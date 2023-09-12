# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        Decent answer
        """
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)




if __name__ == "__main__":
    S = Solution()

    N16 = TreeNode(16)
    N15 = TreeNode(15)
    N14 = TreeNode(14)
    N13 = TreeNode(13, N16)
    N12 = TreeNode(12, N15)
    N11 = TreeNode(11, N14)
    N10 = TreeNode(10)
    N9 = TreeNode(9, left=None, right=N13)
    N8 = TreeNode(8, left=None, right=N12)
    N7 = TreeNode(7, N10, N11)
    N6 = TreeNode(6)
    N5 = TreeNode(5, N9)
    N4 = TreeNode(4, N8)
    N3 = TreeNode(3, N6, N7)
    N2 = TreeNode(2, N4, N5)
    N1 = TreeNode(1, N2, N3)

    print(S.sumOfLeftLeaves(N1))
