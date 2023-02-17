"""
Accumulated Examples For Review Purposes:

"""

class Solution:
    """
    Inorder traversal
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		# left -> root -> right
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []