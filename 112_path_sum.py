#  https://leetcode.com/problems/path-sum/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        if not root:
            return False
        print(f'ROOT VAL OF CURRENT NODE: {root.val}')
        print(f'CURRENT TARGET SUM {targetSum}')
        if not root.left and not root.right:
            print(f'LEAF AT {root.val}')
            return print(f'This is the return call: {targetSum - root.val == 0}')
        return self.hasPathSum(root.left, targetSum - root.val)
        print(f'ROOT VAL AFTER RETURN FROM LEFT RECURSION: {root.val}')
        self.hasPathSum(root.right, targetSum - root.val)
        print(f'ROOT VAL AFTER RETURN FROM RIGHT RECURSION: {root.val}')


if __name__ == '__main__':
    N1 = TreeNode(1)
    N2 = TreeNode(2)
    N3 = TreeNode(3)
    N4 = TreeNode(4)
    N5 = TreeNode(5)
    N6 = TreeNode(6)
    N7 = TreeNode(7)
    N8 = TreeNode(8)

    N1.left = N2
    N1.right = N3
    N2.left = N4
    N2.right = N5
    N3.left = N6
    N3.right = N7
    N7.right = N8

    L1 = TreeNode(5)
    L2 = TreeNode(4)
    L3 = TreeNode(8)
    L4 = TreeNode(11)
    L5 = TreeNode(13)
    L6 = TreeNode(4)
    L7 = TreeNode(7)
    L8 = TreeNode(2)
    L9 = TreeNode(1)

    L1.left = L2
    L1.right = L3
    L2.left = L4
    L3.left = L5
    L3.right = L6
    L4.left = L7
    L4.right = L8
    L6.right = L9

    S = Solution()
    print(S.hasPathSum(N1, 10))