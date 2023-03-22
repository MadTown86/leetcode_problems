# https://leetcode.com/problems/balanced-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# function to find height of binary tree, had to find elsewhere. However, I should now have it fairly memorized

class Solution:
    def height(self, root):

        # base condition when binary tree is empty
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    # function to check if tree is height-balanced or not


    def isBalanced(self, root):

        # Base condition
        if root is None:
            return True

        # for left and right subtree height
        lh = self.height(root.left)
        rh = self.height(root.right)

        # allowed values for (lh - rh) are 1, -1, 0
        if (abs(lh - rh) <= 1) and self.isBalanced(
                root.left) is True and self.isBalanced(root.right) is True:
            return True

        # if we reach here means tree is not
        # height-balanced tree
        return False



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(8)
    S = Solution()
    if S.isBalanced(root):
        print("Tree is balanced")
    else:
        print("Tree is not balanced")


    N1 = TreeNode(3)
    N2 = TreeNode(9)
    N3 = TreeNode(20)
    N4 = TreeNode(15)
    N5 = TreeNode(7)
    N6 = TreeNode(8)

    N1.left = N2
    N1.right = N3
    N2.left = N4
    N2.right = N5
    N4.left = N6


    S2 = Solution()
    print(S.isBalanced(N1))