class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    flag = True

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Mergesort with recursion

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def recurseit(nums):
            if len(nums) <= 1:
                return

            mid = len(nums) // 2
            left_end = nums[:mid]
            right_end = nums[mid:]

            left_index = 0
            right_index = 0
            base_index = 0

            recurseit(left_end)
            recurseit(right_end)

            while left_index < len(left_end) and right_index < len(right_end):
                if left_end[left_index] < right_end[right_index]:
                    nums[base_index] = left_end[left_index]
                    left_index += 1
                else:
                    nums[base_index] = right_end[right_index]
                    right_index += 1
                base_index += 1

            if left_index < len(left_end):
                del nums[base_index:]
                nums += left_end[left_index:]
            if right_index < len(right_end):
                del nums[base_index:]
                nums += right_end[right_index:]

        recurseit(nums)
        return nums