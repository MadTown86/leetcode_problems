class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        newTree = TreeNode(val=root.val)
        head_newTree = newTree
        cursor = root
        left_stack = [root.left]
        right_stack = [root.right]






if __name__ == "__main__":
    N15 = TreeNode(15)
    N14 = TreeNode(14)
    N13 = TreeNode(13)
    N12 = TreeNode(12)
    N11 = TreeNode(11)
    N10 = TreeNode(10)
    N9 = TreeNode(9)
    N8 = TreeNode(8)
    N7 = TreeNode(7, N14, N15)
    N6 = TreeNode(6, N12, N13)
    N5 = TreeNode(5, N10, N11)
    N4 = TreeNode(4, N8, N9)
    N3 = TreeNode(3, N6, N7)
    N2 = TreeNode(2, N4, N5)
    NRoot = TreeNode(1, N2, N3)

