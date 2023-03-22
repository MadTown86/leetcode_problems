# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.visited = []
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root.left and not root.right:
            return []
        if root.left and root.right:
            return [[z, y] for z in [z for z in self.levelOrder(root.left)] for y in [x for x in self.levelOrder(root.right)]] + [root.val]
        if root.left and not root.right:
            return [x for x in self.levelOrder(root.left)] + [root.val]
        if root.right and not root.left:
            return [y for y in self.levelOrder(root.right)] + [root.val]
        return [root.val]



"""
#Other iterative approach I should have gone after.  Eventually, I 'knew' that you would need to have multiple layers of recursion in order to track depth
but couldn't get it.

def levelOrder(self, root):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])
        LRpair = [(node.left, node.right) for node in level]
        level = [leaf for LR in LRpair for leaf in LR if leaf]
    return ans


# https://leetcode.com/problems/binary-tree-level-order-traversal/solutions/33464/5-6-lines-fast-python-solution-48-ms/?orderBy=most_votes&languageTags=python

I  had to look it up, the recursive way to do it I knew was something like this but couldn't nail it down after a while.

I need to remember this.

def levelOrder(self, root):
        if not root:
            return []
        
        answer = []
        self.traverse(root, 1, answer)
        return answer
    
    def traverse(self, node, level, answer):
        if not node:
            return 
        
        if level > len(answer):
            # we are at a new level
            answer.append([node.val])
        else:
            answer[level-1].extend([node.val])
        
        self.traverse(node.left, level + 1, answer)
        self.traverse(node.right, level + 1, answer)    
"""



if __name__ == '__main__':
    N1 = TreeNode(3)
    N2 = TreeNode(9)
    N3 = TreeNode(20)
    N4 = TreeNode(15)
    N5 = TreeNode(7)

    N1.left = N2
    N1.right = N3
    N2.left = N4
    N2.right = N5

    S = Solution()
    print(S.levelOrder(N1))
