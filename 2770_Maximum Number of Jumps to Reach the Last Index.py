# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        counted = []
        if -target <= nums[0] - nums[-1] <= target and len(nums) > 1:
            counted.append(1)
        def traverse(nums: List[int], target: int, count: int) -> int:
            # print(f'{nums=}')
            if len(nums) == 1:
                counted.append(count)
            for x in range(len(nums)-1):
                for j in range(1, len(nums)-x):
                    if -target <= nums[x] - nums[x+j] <= target:
                        if nums[x + j]
                        traverse(nums[x+1:], target, count + 1)

        traverse(nums, target, 0)
        return -1 if len(counted) == 0 else max(counted)


if __name__ == "__main__":
    input = ([1, 3, 6, 4, 1, 2], 2)
    inp6 = ([1, 3, 5, 7, 9, 11], 2)
    inp7 = ([1, 4, 6, 10, 9, 13, 25, 12], 3)
    inp2 = ([1, 3, 1, 4, 1, 6, 1, 7, 5], 2)
    inp3 = ([1, 3, 6, 4, 1, 2], 3)
    inp5 = ([1, 3, 6, 4, 1, 2], 0)
    inp4 = ([1, 0, 2], 1)
    inptest = ([1, -1, -3, -4, -6, -7, -8], 2)

    S = Solution()
    print(S.maximumJumps(*input))
    # print(S.maximumJumps(*inp2))
    print(S.maximumJumps(*inp3))
    print(S.maximumJumps(*inp4))
    print(S.maximumJumps(*inp5))
    # print(S.maximumJumps(*inp6))
    # print(S.maximumJumps(*inp7))
    # print(S.maximumJumps(*inptest))


