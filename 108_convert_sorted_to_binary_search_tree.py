# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List



#I am still missing the point of this.  I guess you would want to always build the
#Tree from left to right, making sure that the tree is as compact as possible.
#
"""
OTHER ANSWERS: 

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node], 
            self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1 :])
        )
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.makeBST(nums, 0, len(nums))
    
    def makeBST(self, nums, start, end):
        if start >= end: return None
        return TreeNode(
            val=nums[ (start + end)//2 ],
            left=self.makeBST(nums, start, (start + end)//2),
            right=self.makeBST(nums, 1+((start+end)//2), end)
        )
        
chatGPT:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        print(f'MIDDLE VALUE: {nums[mid]}')
        print(f'LEFT SIDE: {nums[:mid]}')
        print(f'RIGHT SIDE: {nums[mid+1:]}')
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


# class Solution:
#     def __init__(self):
#         self.root = None
#         self.left_l = 0
#         self.right_l = 0
#
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         if len(nums) == 0:
#             return TreeNode(nums.pop())
#
#         if len(nums) == 2:
#             if nums[0] > nums[1]:
#                 self.root = TreeNode(nums[0])
#                 self.root.left = TreeNode(nums[1])
#                 return self.root
#             else:
#                 self.root = TreeNode(nums[1])
#                 self.root.right = TreeNode(nums[0])
#                 return self.root
#
#         if nums and len(nums) > 1:
#             mid = len(nums) // 2
#             left = nums[:mid]
#             right = nums[mid+1:]
#
#         self.root = TreeNode(mid)
#
#         print(f"INPUT :::: {nums}")
#         print(f"LEFT: {left}")
#         print(f"RIGHT: {right}")
#         print(f"ROOT: {self.root.val}")
#         print(f'ROOT LEFT: {self.root.left.val if self.root.left else "None"}')
#         print(f'ROOT RIGHT: {self.root.right.val if self.root.right else "None"}')
#
#         # Check split point to ensure adheres to Height balanced binary tree
#         root_for_right = self.root
#         root_for_left = self.root
#         prev_right_node = root_for_right
#         prev_left_node = root_for_left
#         flag = False
#         while left and right:
#             if left:
#                 left_curr = left.pop()
#                 root_for_left.left = TreeNode(left_curr)
#                 self.left_l += 1
#                 prev_left_node = root_for_left
#                 root_for_left = root_for_left.left
#             if right:
#                 right_curr = right.pop()
#                 root_for_right.right = TreeNode(right_curr)
#                 self.right_l += 1
#                 prev_right_node = root_for_right
#                 root_for_right = root_for_right.right
#
#             if left and not right:
#                 left_curr = left.pop()
#                 root_shadow = self.root
#                 while root_shadow.left is not prev_left_node and root_shadow.left is not None:
#                     print('stepped in lefts shadow')
#                     root_shadow = root_shadow.left
#                 root_shadow.left = root_for_left
#                 root_for_left.right = prev_left_node
#                 root_for_left.left = TreeNode(left_curr)
#
#             if right and not left:
#                 right_curr = right.pop()
#                 root_shadow = self.root
#                 while root_shadow.right is not prev_right_node:
#                     print('stepped in rights shadow')
#                     root_shadow = root_shadow.right
#                 root_shadow.right = root_for_right
#                 root_for_right.left = prev_right_node
#                 root_for_right.right = TreeNode(right_curr)
#
#         print(f"INPUT :::: {nums}")
#         print(f"LEFT: {left}")
#         print(f"RIGHT: {right}")
#         print(f"ROOT: {self.root.val}")
#         print(f'ROOT LEFT: {self.root.left.val if self.root.left else "None"}')
#         print(f'ROOT RIGHT: {self.root.right.val if self.root.right else "None"}')
#
#         return self.root
#
#     def _printit(self, root: TreeNode) -> List:
#         s = []
#         ret = []
#         print(f"ROOT: {root.val}")
#         ret.append(root.val)
#         visited_left = []
#         visited_right = []
#         if root.left and root.right:
#             s.append(root.left)
#             s.append(root.right)
#         elif root.left and not root.right:
#             s.append(root.left)
#         else:
#             s.append(root.right)
#
#         while s:
#             curr = s.pop(0)
#             print(curr.val)
#             ret.append(curr.val)
#             if curr.left is not None and curr.left not in visited_left:
#                 visited_left.append(curr.left)
#                 s.append(curr.left)
#             else:
#                 ret.append(None)
#                 print(None)
#             if curr.right is not None and curr.right not in visited_right:
#                 visited_right.append(curr.right)
#                 s.append(curr.right)
#             else:
#                 ret.append(None)
#                 print(None)
#
#         return ret
#

if __name__ == "__main__":
    examp = [-10, -3, 0, 5, 9]
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    arr2 = [-3, -2, -1, 0, 1, 2, 3, 4]
    S = Solution()
    arrayit = S.sortedArrayToBST(arr)
    arrt = S._printit(arrayit)
    print(arrt)
    # S.sortedArrayToBST(arr2)
    # S.sortedArrayToBST(examp)

