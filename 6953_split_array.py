# https://leetcode.com/contest/weekly-contest-357/problems/check-if-it-is-possible-to-split-array/

from typing import List
from itertools import pairwise


class Solution:
    def canSplitArray2(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        flag = False
        stack = [nums]
        spl = len(nums) // 2
        while stack:
            print(f"{stack=}")
            sub_array = stack.pop()
            print(f"{sub_array=}")
            if len(sub_array) == 2 and sub_array[0] == sub_array[1]:
                return True
            # if len(sub_array) == 1:
            #     continue
            for x in range(len(sub_array) - 1):
                print(f"{x=}")
                print(f"{sub_array[x]=} :: {sub_array[x + 1]}")
                if sub_array[x] == sub_array[x + 1] and len(sub_array) > 1:
                    flag = True
                    if x + 1 != len(sub_array) - 1:
                        first, second = sub_array[: x + 2], sub_array[x + 2 :]
                    else:
                        print("here")
                        first, second = sub_array[-x - 1 :], sub_array[: -x - 1]
                    print(f"{first=}")
                    print(f"{second=}")
                    if sum(first) >= m:
                        stack.append(first)
                    if sum(second) >= m:
                        stack.append(second)
                    break

            if not flag:
                if len(nums) > 2:
                    spl = len(nums) // 2
                    first, second = nums[: spl + 1], nums[spl + 1 :]
                else:
                    first, second = [nums[0]], [nums[1]]
                if sum(first) > m:
                    stack.append(first)
                    print(f" HALVED: {first=}")
                if sum(second) > m:
                    stack.append(second)
                    print(f"HAVLED {second=}")
                flag = False

        return False

    def canSplitArray(self, nums: List[int], m):
        if 0 < len(nums) < 2:
            return True
        for x, y in pairwise(nums):
            if x == y:
                return True
        def f(x):
            if
        return False


if __name__ == "__main__":
    S = Solution()

    inputs = [([2, 2, 1], 4), ([2, 1, 3], 5), ([2, 3, 3, 2, 3], 6), ([9, 7], 1)]

    print(S.canSplitArray(*inputs[3]))
    # print(S.canSplitArray(*inputs[1]))
    # for x in inputs:
    #     S.canSplitArray(*x)
    #
    # assert S.canSplitArray(*inputs[0]) == True
    # assert S.canSplitArray(*inputs[1]) == False
    # assert S.canSplitArray(*inputs[2]) == True
