# https://leetcode.com/problems/balanced-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        if root is None:
            return root

        return max(self.isBalanced(root.left), self.isBalanced(root.right))

    def height(self, root) -> bool:
        if root is None:
            return True

        lh = self.isBalanced(root.left)
        rh = self.isBalanced(root.right)

        if (abs(lh - rh) <= 1) and self.height(root.left) is True and self.height(root.right) is True:
            return True

        return False

if __name__ == '__main__':
    N1 = TreeNode(3)
    N2 = TreeNode(9)
    N3 = TreeNode(20)
    N4 = TreeNode(15)
    N5 = TreeNode(7)


    L1 = TreeNode(1)
    L2 = TreeNode(

    )