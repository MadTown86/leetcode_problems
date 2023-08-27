from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        # Outer Layer - Search for potential sublists that needs to run after each operational push
        a, b = 0, 1
        while True:
            potential_sublists = []
            while b < len(nums):
                if b == len(nums) - 1:
                    summed = sum(nums[a:])
                    splice = nums[a:]
                else:
                    summed = sum(nums[a : b + 1])
                    splice = nums[a : b + 1]
                if summed > target:
                    divisible_list = []
                    for index in range(a, b + 1):
                        if nums[index] % 2 == 0:
                            divisible_list.append((index, nums[index]))
                    if not divisible_list:
                        a += 1
                    else:
                        for ind, value in divisible_list:
                            if summed - value < target:
                                potential_sublists.append(splice)

        operation_count = 0
        i, j = 0, 1
        while j < len(nums):
            if j == len(nums) - 1:
                summed = sum(nums[i:])
                splice = nums[i:]
            else:
                summed = sum(nums[i : j + 1])
                splice = nums[i : j + 1]
            if summed > target:
                divisible_list = []
                for index in range(i, j + 1):
                    if nums[index] % 2 == 0:
                        divisible_list.append((index, nums[index]))
                if not divisible_list:
                    i += 1
                else:
                    for ind, value in divisible_list:
                        if summed - value < target:
                            halved = value // 2
                            nums[ind] = halved
                            nums.insert(ind, halved)
                            operation_count += 1
                            break
            if summed == target:
                return operation_count
            if summed < target:
                j += 1

        return -1


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

    S = Solution()
    # S.minOperations(*inputs[0])
    S.minOperations(*inputs[1])
    # assert S.minOperations(*inputs[0]) == 1
    # assert S.minOperations(*inputs[1]) == 2
    # assert S.minOperations(*inputs[2]) == -1
