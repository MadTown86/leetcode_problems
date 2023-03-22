"""
Accumulated Examples For Review Purposes:

"""
from typing import List
class Solution:
    """
    Inorder traversal
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
		# left -> root -> right
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

#https://leetcode.com/problems/maximum-depth-of-binary-tree/

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

    # self. maxDepth(None) = 0 by definition

    self.maxDepth(10)
    max(self.maxDepth(5), self.maxDepth(19)) + 1  # First recursive call from node 10
    max(max(self.maxDepth(None), self.maxDepth(None)) + 1,
        self.maxDepth(19)) + 1  # Recursive call on node 5 and its expansion
    max(1, self.maxDepth(19)) + 1  # Replacing for self. maxDepth(None) = 0
    max(1, max(self.maxDepth(17), self.maxDepth(None)) + 1) + 1  # Recursive call from node 19
    max(1, max(self.maxDepth(17), 0) + 1) + 1  # Replacing for self. maxDepth(None) = 0
    max(1, max(max(self.maxDepth(None), self.maxDepth(None)) + 1, 0) + 1) + 1  # Recursive call from node 17
    max(1, max(max(0, 0) + 1, 0) + 1) + 1  # Replacing for self. maxDepth(None) = 0
    max(1, max(0 + 1, 0) + 1) + 1  # Replacing the inner most max
    max(1, 1 + 1) + 1  # Replacing the inner most max
    max(1, 2) + 1
    2 + 1  # Replacing the inner most max

# https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search_/_level_order


"""
This following one is for checking if a binary tree is height balanced:
class Solution:
    def height(self, root):

        # base condition when binary tree is empty
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    # function to check if tree is height-balanced or not


    def isBalanced(self, root):

        # Base condition
        if root is None:
            return True

        # for left and right subtree height
        lh = self.height(root.left)
        rh = self.height(root.right)

        # allowed values for (lh - rh) are 1, -1, 0
        if (abs(lh - rh) <= 1) and self.isBalanced(
                root.left) is True and self.isBalanced(root.right) is True:
            return True

        # if we reach here means tree is not
        # height-balanced tree
        return False
"""

"""
Design Pattern:
Depth-First-Search
1. If the current node is emty then return
2. Execute the following three operations in a certain order:
    N. Visit the current node
    L. Recursively traverse the current node's left subtree
    R. Recursively traverse the current node's rigth subtree
"""
