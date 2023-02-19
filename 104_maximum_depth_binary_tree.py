from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    maxs = 0
    c = 0
    traversed = []
    def maxDepth(self, root: TreeNode) -> int:
        self._maxDepth(root)
        return self.maxs
    def _maxDepth(self, root: TreeNode) -> int:
        if root is not None:
            print(root.val)
            self.c += 1
            if root.left is None and root.right is None:
                self.traversed.append(root)
            if root.left not in self.traversed:
                self._maxDepth(root.left)
            if root.left in self.traversed and root.right is not None and root.right not in self.traversed:
                self._maxDepth(root.right)

        else:
            pass


"""
I had to look it up
"""

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        worklist = deque([root])
        num_node_level = 1
        levels = 0
        while worklist:
            node = worklist.popleft()
            if node.left:
                worklist.append(node.left)
            if node.right:
                worklist.append(node.right)
            num_node_level -= 1
            if num_node_level == 0:
                levels += 1
                num_node_level = len(worklist)

        return levels





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

    S = Solution()
    print(S.maxDepth(T1))





