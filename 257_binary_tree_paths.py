class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    res_list = set()
    def binaryTreePaths(self, root: TreeNode, outstr) -> str:
        pnter = '->'
        """
        Recursion: 
        If leaf = add to res_list and return
        At every pass determine first whether it is a leaf node (meaning left/right == None)
        if not, then first left - continue the recursion loop
        else right - continue the recursion loop
        """

        if not root:
            res = ''
            for x in range(len(outstr)):
                if x < len(outstr)-1:
                    res += outstr[x] + pnter
                else:
                    res += outstr[x]
            self.res_list.add(res)
            return ''
        return self.binaryTreePaths(root.left, outstr + str(root.val)) + self.binaryTreePaths(root.right, outstr + str(root.val))



if __name__ == "__main__":
    N7 = TreeNode(val=7)
    N6 = TreeNode(val=6)
    N5 = TreeNode(val=5)
    N4 = TreeNode(val=4)
    N3 = TreeNode(val=3, left=N6, right=N7)
    N2 = TreeNode(val=2, left=N4, right=N5)
    N1 = TreeNode(val=1, left=N2, right=N3)

    S = Solution()
    print(S.binaryTreePaths(N1, ''))
    print(S.res_list)

