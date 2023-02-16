from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    r = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self._subtree(root)
        return self.r

    def _subtree(self, root: TreeNode):
        if root.left != None:
            self._subtree(root.left)
        self.r.append(root.val)
        if root.right != None:
            self._subtree(root.right)

"""
Other peoples brilliant answers:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This is a standard in-order traversal problem, I'd suggest to learn pre-order and post-order as well.
# Here's a short tutorial if you're interested.
# https://wingkwong.github.io/leetcode-the-hard-way/tutorials/graph-theory/binary-tree
# then you may try the following problems
# 144. Binary Tree Preorder Traversal: https://leetcode.com/problems/binary-tree-preorder-traversal/
# 145. Binary Tree Postorder Traversal: https://leetcode.com/problems/binary-tree-postorder-traversal/

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		# left -> root -> right
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            return inorder(root.left)+[root.val]+inorder(root.right) if root else []
        return inorder(root)

class Solution:
    def inorder(self,root):
        res,stack=[],[(root,False)]
        while stack:
            node,visited=stack.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node.right,False))
                    stack.append((node,True))
                    stack.append((node.left,False))
        return res
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder(root)