from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        while root.left != None:


if __name__ == '__main__':
    T7 = TreeNode(val = 7)
    T6 = TreeNode(val = 6)
    T5 = TreeNode(val = 5, left=T6, right=T7)
    T4 = TreeNode(val = 4)
    T3 = TreeNode(val = 3)
    T2 = TreeNode(val = 2, left=T3, right=T4)
    T1 = TreeNode(val = 1, left=T2, right=T5)

