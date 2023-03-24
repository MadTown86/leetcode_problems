#  https://leetcode.com/problems/path-sum/

def cacheit(func):
    counter = 0
    def outter(func):
        def inner(node, targetSum, valcarry=0):
            nonlocal counter
            counter += 1
            print(f'VALCARRY: {valcarry}')
            print(f'RECURSIVE LEVEL: {counter}')
            print(f'NODE NAME: {node.name}')
            print(f'NODE VALUE: {node.val}')
            print(f'targetSum: {targetSum}')
            return func(node, targetSum)
        return outter
    return inner
class TreeNode:
    def __init__(self, name: str = None, val=0, left=None, right=None):
        self.name = name
        self.val = val
        self.left = left
        self.right = right
class Solution:

    @cacheit
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root.val:
            print(root.val)
        if not root:
            return 0
        if root.left and root.right:
            return self.hasPathSum(root.left, targetSum) + self.hasPathSum(root.right, targetSum) + root.val
        elif root.left and not root.right:
            return self.hasPathSum(root.left, targetSum) + root.val
        elif root.right and not root.left:
            return self.hasPathSum(root.right, targetSum) + root.val
        else:
            return root.val


if __name__ == '__main__':
    N1 = TreeNode(name="Node 1", val=1)
    N2 = TreeNode(name="Node 2", val=2)
    N3 = TreeNode(name="Node 3", val=3)
    N4 = TreeNode(name="Node 4", val=4)
    N5 = TreeNode(name="Node 5", val=5)
    N6 = TreeNode(name="Node 6", val=6)
    N7 = TreeNode(name="Node 7", val=7)
    N8 = TreeNode(name="Node 8", val=8)

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
    print(S.hasPathSum(N1, 18))