# https://leetcode.com/problems/symmetric-tree/

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        ll, lr, rl, rr, l_stack, r_stack = 0, 0, 0, 0, deque(), deque()
        r_visited, l_visited = [], []

        def leftpass(node, stack, score):
            print(node.val)
            if node.left is not None and node.left not in l_visited:
                stack.appendleft(node.left)
                score += 1
            else:
                score += 1

        def rightpass(node, stack, score):
            print(node.val)
            if node.right is not None and node.right not in r_visited:
                stack.appendleft(node.right)
                score += 1
            else:
                score += 1


        if not root.left and not root.right:
            if not root:
                return False
            else:
                return True
        else:
            s_left = root.left
            l_stack.appendleft(s_left)
            while s_left.left:
                l_stack.appendleft(s_left.left)
                l_visited.append(s_left.left)
                ll += 1
                s_left = s_left.left

            while l_stack:
                pop_right = l_stack.pop()
                if pop_right.left:
                    leftpass(pop_right.left, l_stack, ll)
                    l_visited.append(pop_right)
                if pop_right.right:
                    rightpass(pop_right.right, l_stack, lr)
                    r_visited.append(pop_right)

            s_right = root.right
            r_stack.append(s_right)
            while s_right.right:
                r_stack.append(s_right.right)
                r_visited.append(s_right.right)
                rr += 1
                s_right = s_right.right

            while r_stack:
                pop_onright = r_stack.pop()
                if pop_onright.right:
                    rightpass(pop_onright.right, r_stack, rr)
                    r_visited.append(pop_onright)
                if pop_onright.left:
                    l_visited.append(pop_onright)
                    leftpass(pop_onright.left, r_stack, rl)


        print(f'll: {ll}, lr = {lr}, rr = {rr}, rl = {rl}')


if __name__ == '__main__':
    N7 = TreeNode(6)
    N6 = TreeNode(5)
    N5 = TreeNode(4)
    N4 = TreeNode(3)
    N3 = TreeNode(2)
    N2 = TreeNode(1)
    N1 = TreeNode(0)
    N1.left = N2
    N1.right = N3
    N2.left = N4
    N2.right = N5
    N3.left = N6
    N3.right = N7

    S = Solution()
    print(S.isSymmetric(N1))

