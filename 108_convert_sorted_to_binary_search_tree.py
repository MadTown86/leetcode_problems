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

    def height(self, root):
        if root is None:
            return True

        lh = self.isBalanced(root.left)
        rh = self.isBalanced(root.right)

        if (abs(lh - rh) <= 1) and height(root.left) is True and height(root.right) is True:
            return True

        return False

