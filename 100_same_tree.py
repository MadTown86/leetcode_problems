class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    flag = True

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)








if __name__ == "__main__":
    T9 = TreeNode(val=9)
    T8 = TreeNode(val=8, right=T9)
    T7 = TreeNode(val=7, right=T8)
    T6 = TreeNode(val=6)
    T5 = TreeNode(val=5, left=T6, right=T7)
    T4 = TreeNode(val=4)
    T3 = TreeNode(val=3)
    T2 = TreeNode(val=2, left=T3, right=T4)
    T1 = TreeNode(val=1, left=T2, right=T5)

    L9 = TreeNode(val=9)
    L8 = TreeNode(val=8, right=L9)
    L7 = TreeNode(val=7, right=L8)
    L6 = TreeNode(val=6)
    L5 = TreeNode(val=5, left=L6, right=L7)
    L4 = TreeNode(val=4)
    L3 = TreeNode(val=3)
    L2 = TreeNode(val=2, left=L3, right=L4)
    L1 = TreeNode(val=1, left=L2, right=L5)

    S = Solution()
    print(S.isSameTree(p=L1, q=T1))