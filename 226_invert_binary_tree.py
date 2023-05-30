from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        new_Tree = TreeNode(val=root.val)
        left_Tree = None
        right_Tree = None
        print_stack = []
        l, r = root.left, root.right
        print_stack.append(((root.val, (l.val, r.val))))
        loop_stack = [(l, r)]
        while loop_stack:
            l, r = loop_stack.pop()
            if l and l.left and l.right:
                l_inp = (l.val, (l.left.val, l.right.val))
                if l_inp not in print_stack:
                    print_stack.append(l_inp)
                    loop_stack.append((l.left, l.right))
            if r and r.left and r.right:
                r_inp = (r.val, (r.left.val, r.right.val))
                if r_inp not in print_stack:
                    print_stack.append(r_inp)
                    loop_stack.append((r.left, r.right))

    def invertTree2(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        new_Tree = root
        n_T = new_Tree
        traversed = []
        stack = [root.left, root.right]

        while stack:
            r, l = stack.pop()
            new_node = TreeNode(val=r.val, left=r.right, right=r.left)
            n_T.right = new_node















        print(print_stack)

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

    S = Solution()
    S.invertTree(NRoot)

