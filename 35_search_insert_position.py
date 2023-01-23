from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        def recurse_inner(target, left, right):
            print(nums[left:right+1])
            print(f'LEFT: {left}')
            print(f'RIGHT {right}')
            r_len = right - left


        return recurse_inner(target, left, right)

if __name__ == "__main__":
    S = Solution()
    args = [([1, 3, 5, 6], 5), ([1, 3, 5, 6], 2), ([1, 3, 5, 6], 7)]
    for tups in args:
        print(S.searchInsert(*tups))
