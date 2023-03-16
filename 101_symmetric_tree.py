# https://leetcode.com/problems/symmetric-tree/

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.r_right = 0
        self.r_left = 0
    def isSymmetric(self, root: TreeNode) -> bool:
        l_stack, r_stack = deque(), deque()
        r_visited, l_visited = [], []

        if root and not root.left and not root.right:
            return True
        if not root or not root.left or not root.right:
            return False
        root_right = root

        # Prime left side deque, add nodes to left_visited
        while root.left:
            l_stack.append(root.left)
            l_visited.append(root.left)
            self.left += 1
            root = root.left
        # Prime right side deque, add nodes to right_visited
        while root_right.right:
            r_stack.append(root_right.right)
            r_visited.append(root_right.right)
            self.r_right += 1
            root_right = root_right.right

        # Pop through left side deque until empty, adding new nodes when not already in visited bins
        while l_stack and r_stack:
            curr_node = l_stack.popleft()
            curr_right_node = r_stack.popleft()

            if curr_node.val != curr_right_node.val:
                return False

            if curr_node.left and curr_node.left not in l_visited:
                l_stack.appendleft(curr_node.left)
                l_visited.append(curr_node.left)
                self.left += 1
            if curr_node.right and curr_node.right not in r_visited:
                l_stack.appendleft(curr_node.right)
                r_visited.append(curr_node.right)
                self.right += 1

            if curr_right_node.right and curr_right_node.right not in r_visited:
                r_stack.appendleft(curr_right_node.right)
                r_visited.append(curr_right_node.right)
                self.r_right += 1
            if curr_right_node.left and curr_right_node.left not in l_visited:
                r_stack.appendleft(curr_right_node.left)
                l_visited.append(curr_right_node.left)
                self.r_left += 1

            if self.left != self.r_right or self.right != self.r_left:
                return False

        return True if self.left == self.r_right and self.right == self.r_left and not l_stack and not r_stack else False

# Recursive Answer from Submissions:
# https://leetcode.com/problems/symmetric-tree/solutions/33068/6line-ac-python/?orderBy=most_votes&languageTags=python

"""
    def isSymmetric(self, root):
        def isSym(L,R):
            if not L and not R: return True
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root, root)
"""

"""
def isSymmetric(self, root):
    if not root:
        return True
    return self.dfs(root.left, root.right)
    
def dfs(self, l, r):
    if l and r:
        return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
    return l == r
	
def isSymmetric(self, root):
    if not root:
        return True
    stack = [(root.left, root.right)]
    while stack:
        l, r = stack.pop()
        if not l and not r:
            continue
        if not l or not r or (l.val != r.val):
            return False
        stack.append((l.left, r.right))
        stack.append((l.right, r.left))
    return True
"""



if __name__ == '__main__':

    # False Case - [2,-4,-4,null,-79,null,-79,-37,null,-37]
    N10 = TreeNode(-37)
    N9 = None
    N8 = TreeNode(-37)
    N7 = TreeNode(-79)
    N6 = None
    N5 = TreeNode(-79)
    N4 = None
    N3 = TreeNode(-4)
    N2 = TreeNode(-4)
    N1 = TreeNode(2)
    N1.left = N2
    N1.right = N3
    N2.left = N4
    N2.right = N5
    N3.left = N6
    N3.right = N7
    N5.left = N8
    N5.right = N9
    N7.left = N10
    N7.right = None

    L7 = TreeNode(6)
    L4 = TreeNode(6)
    L6 = TreeNode(5)
    L5 = TreeNode(5)
    L3 = TreeNode(4)
    L2 = TreeNode(4)
    L1 = TreeNode(2)

    L1.left = L2
    L1.right = L3
    L2.left = L4
    L2.right = L5
    L3.left = L6
    L3.right = L7

    S = Solution()
    print(S.isSymmetric(L1))

