# https://leetcode.com/contest/weekly-contest-360/problems/minimum-operations-to-form-subsequence-with-target-sum/

from typing import List
from itertools import permutations


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        # Outer Layer - Search for potential sublists that needs to run after each operational push

        # This rearranged the list to provide a pivot point between adding numbers that can be divided and those that can't
        def arrange(nums):
            """
            This is just my own sorting algorithm that arranges the array in increasing order and separates
            the values that aren't divisible by 2, thereby not being squares of 2

            Input: array
            Return-
            front_mark -> int: the location where the last value that isn't divisible by 2 resides
            """
            back_mark = len(nums) - 1
            cursor = 0
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

            front_mark = cursor
            return front_mark

        # This function will divide a squares in 2, remove the original value and add the two separate value to the end.
        def divide_squares(index: int, nums: List[int]) -> None:
            nonlocal back_mark
            halved = nums[index] // 2
            nums.pop(index)
            nums.append(halved)
            nums.append(halved)
            back_mark -= 1

        def permutations_front(nums: List[int], operations_count: int) -> int:
            i = 0
            while i < front_mark - 1:
                core_sum = nums[i]
                b = i + 1
                permute_sum = 0
                offset_count = 0
                while b != front_mark:
                    if permute_sum + core_sum == target:
                        return operations_count
                    elif permute_sum + core_sum < target:
                        permute_sum += nums[b + offset_count]
                        b += 1
                    elif permute_sum + core_sum > target:
                        offset_count += 1
                        permute_sum = 0
                        b = i + 1
                i += 1

        def permutations_all(nums: List[int], operations_count: int) -> int:
            i = 0
            while i < len(nums)-1:
                core_sum = nums[i]
                b = i + 1
                permute_sum = 0
                offset_count = 0
                while b != len(nums)-1:



        front_mark = arrange(nums)
        summed = 0
        operations_count = 0
        a = 0
        while a < len(nums):
            end = len(nums)
            difference = abs(summed - target)

            # If index is less than the end of the range of numbers not divisible by 2
            if a < front_mark:
                if nums[a] < difference:
                    summed += nums[a]
                    a += 1
                    continue
                elif nums[a] > difference:
                    interim_sum = summed

                    # Front End Search Portion - try all combinations of units not squares first

                    # Front Offset Search - exact match
                    front_cursor = 0
                    front_list = []
                    offset = (summed + nums[a]) - target
                    while front_cursor != a:
                        if nums[front_cursor] == offset:
                            return operations_count
                        front_list.append(nums[front_cursor])
                        front_cursor += 1

                    # Permutations Search Front Only

                    permutations_front(nums, operations_count)

            # If index a is at the indexes that are divisible by 2 and past the 'front'
            else:
                # If the difference is divisible by 2, then proceed to check squares
                if difference % 2 == 0:
                    b = front_mark
                    while b >= end - 1:
                        if nums[b] < difference:
                            summed += nums[b]
                            a += 1
                            continue
                        if nums[b] / 2 == difference:
                            operations_count += 1
                            return operations_count
                        elif nums[b] / 2 < difference:
                            if nums[b] / 2 == 1:
                                nums.pop(b)
                                nums.insert(b, 1)
                                nums.insert(b, 1)
                                operations_count += 1
                            else:
                                divide_squares(b, nums)
                                front_mark, back_mark = arrange(nums)
                                operations_count += 1

                if difference % 2 != 0:
                    permutations_front(nums, operations_count)
                    if nums[a]

            a += 1



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
