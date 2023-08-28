# https://leetcode.com/contest/weekly-contest-360/problems/minimum-operations-to-form-subsequence-with-target-sum/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        # Outer Layer - Search for potential sublists that needs to run after each operational push
        back_mark = len(nums) - 1
        cursor = 0
        trans_a = 0
        trans_b = 0
        while cursor < back_mark:
            if nums[cursor] % 2 == 0:
                trans_val = nums.pop(cursor)
                nums.append(trans_val)
                trans_a = len(nums) - 1
                trans_b = trans_a - 1
                back_mark -= 1
                while trans_b != cursor:
                    if nums[trans_b] > nums[trans_a] and nums[trans_b] % 2 == 0:
                        transfer = nums[trans_b]
                        nums[trans_b] = nums[trans_a]
                        nums[trans_a] = transfer
                        trans_a -= 1
                        trans_b -= 1
                    else:
                        break
            else:
                cursor += 1

        summed = 0
        operations_count = 0
        a, b = 0, 1
        c, d = back_mark, back_mark + 1
        while a < len(nums):
            if summed + nums[a] < target:
                summed += nums[a]
                a += 1
            if summed + nums[a] > target:

                b = a - 1
                while b >= 0:





"""
nums - non-negative powers of 2 and an integer target

One Operation - Limiter
Perform all following
1. Choose any element of the array nums[i] such that nums[i] > 1
2. Remove nums[i] from the array
3. Add two occurrences of nums[i] / 2 to the end of nums

Return minimum number of operations you need to perform sot hat nums contains a subsequence whose elements sum to target
If impossible return -1



"""

if __name__ == "__main__":
    inputs = [([1, 2, 8], 7), ([1, 32, 1, 2], 12), ([1, 32, 1], 35), ([1, 1, 8, 1], 5)]

    arrange = ([1, 32, 3, 16, 36, 4, 5, 64], 10)

    S = Solution()
    S.minOperations(*arrange)
    # S.minOperations(*inputs[0])
    # S.minOperations(*inputs[1])
    # assert S.minOperations(*inputs[0]) == 1
    # assert S.minOperations(*inputs[1]) == 2
    # assert S.minOperations(*inputs[2]) == -1
