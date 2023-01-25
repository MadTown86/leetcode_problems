from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        if len(nums) == 1:
            return 0 if nums[0] >= target else 1

        def recurse_inner(target, left, right, last=None):
            if right - left > 1:
                pos = ((right - left) // 2) + left

                if nums[pos] == target:
                    return pos
                if nums[pos] > target:
                    right = pos
                    last = "L"
                    return recurse_inner(target, left, right, last)
                if nums[pos] < target:
                    left = pos
                    last = "G"
                    return recurse_inner(target, left, right, last)

            elif last == "G" and right - left == 1:
                if target <= nums[right]:
                    return right
                else:
                    return right + 1
            elif last == "L" and right - left == 1:
                if target > nums[left]:
                    return right
                if target <= nums[left]:
                    return left

            else:
                return 0 if nums[0] >= target else 1 if target <= nums[1] else 2

        return recurse_inner(target, left, right)

    def searchInsert1(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        if right == 1:
            return 0 if nums[0] >= target else 1

        if len(nums) == 2:
            if target <= nums[0]:
                return 0
            if target <= nums[1]:
                return 1
            else:
                return 2

        pos = right // 2
        cv = nums[pos]
        if cv == target:
            return pos
        if cv > target:
            return self.searchInsert1(nums[left:pos], target)
        if cv < target:
            return pos + self.searchInsert1(nums[pos:right], target)


    """
    Best answer from Leetcode:
    """

    def searchInsertBest(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                end = mid - 1
            else:
                start = mid + 1
        return start





if __name__ == "__main__":
    from time import perf_counter
    S = Solution()
    args = [([1, 3, 5, 6], 5), ([1, 3, 5, 6], 2), ([1, 3, 5, 6], 7), ([1, 3, 5], 1)]
    for tups in args:
        start = perf_counter()
        print(S.searchInsert1(*tups))
        stop = perf_counter()

        start2 = perf_counter()
        print(S.searchInsert(*tups))
        stop2 = perf_counter()

        start3 = perf_counter()
        print(S.searchInsertBest(*tups))
        stop3 = perf_counter()

        print(f'#2: {stop - start:.10f}')
        print(f'#1: {stop2 - start2:.10f}')
        print(f'#3: {stop3 - start3:.10f}')


