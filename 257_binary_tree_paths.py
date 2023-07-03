from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res_list = set()
        pnter = '->'
        """
        Recursion: 
        If leaf = add to res_list and return
        At every pass determine first whether it is a leaf node (meaning left/right == None)
        if not, then first left - continue the recursion loop
        else right - continue the recursion loop
        """
        def traverse(root: TreeNode, outstr) -> List[str]:
            print(outstr)
            if not root.left and not root.right:
                res = ''
                outstr += [str(root.val)]
                for x in range(1, len(outstr)):
                    if x < len(outstr)-1:
                        res += outstr[x] + pnter
                    else:
                        res += outstr[x]
                res_list.add(res)
                return res
            if root.left:
                traverse(root.left, outstr + [str(root.val)])
            if root.right:
                traverse(root.right, outstr + [str(root.val)])
            return ['']

        traverse(root, [''])
        l = [x for x in res_list]
        return l



if __name__ == "__main__":
    N7 = TreeNode(val=70)
    N6 = TreeNode(val=60)
    N5 = TreeNode(val=50)
    # N4 = TreeNode(val=4)
    N3 = TreeNode(val=30, left=N6, right=N7)
    N2 = TreeNode(val=20, right=N5)
    N1 = TreeNode(val=10, left=N2, right=N3)

    # Test Input [37,-34,-48,null,-100,-100,48,null,null,null,null,-54,null,-71,-22,null,null,null,8]

    S = Solution()
    doeswegotit = S.binaryTreePaths(N1)
    print(doeswegotit)


