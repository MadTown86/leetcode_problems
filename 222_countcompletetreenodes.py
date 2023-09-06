# https://leetcode.com/problems/count-complete-tree-nodes/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # print(root.val)
        if not root:
            return 0
        counter = 0
        if root.left and root.right:
            left = root.left
            right = root.right

        while left.left and right.right:
            last_left = left
            last_right = right
            left = left.left
            right = right.right
            counter += 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1




if __name__ == "__main__":
    S = Solution()
    N12 = TreeNode(12)
    N11 = TreeNode(11)
    N10 = TreeNode(10)
    N9 = TreeNode(9)
    N8 = TreeNode(8)
    N7 = TreeNode(7)
    N6 = TreeNode(6, N12)
    N5 = TreeNode(5, N10, N11)
    N4 = TreeNode(4, N8, N9)
    N3 = TreeNode(3, N6, N7)
    N2 = TreeNode(2, N4, N5)
    N1 = TreeNode(1, N2, N3)

    print(S.countNodes(N1))