# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

from typing import List
from itertools import pairwise
from functools import cache


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        count_max = 0

        @cache
        def traverse(nums, target, count):
            nonlocal count_max
            if len(nums) == 1:
                if count > count_max:
                    count_max = count
            for x in range(1, len(nums)):
                if -target <= nums[x] - nums[0] <= target:
                    traverse(nums[x:], target, count + 1)
                if x == len(nums) - 1 and -target <= nums[x] - nums[0] <= target:
                    count += 1
                    if count > count_max:
                        count_max = count

        traverse(nums, target, 0)
        return count_max if count_max > 0 else -1

    def maximumJumps2(self, nums: List[int], target: int) -> int:
        a, b, c = 0, 1, 2
        n = len(nums)

        count = 0
        cond = lambda x, y: -target <= nums[y] - nums[x] <= target

        for a in range(len(nums)):
            if a > 0 and not cond(0, a):
                continue
            b = a + 1
            while b <= n - 1:
                print(f"{a=} : {b=}")
                inner_count = 0
                if cond(a, b) and b != n - 1:
                    c = b + 1
                    inner_count += 1
                    while c <= n - 1:
                        if cond(b, c) and c != n - 1:
                            inner_count += 1
                            b += 1
                            c = b + 1
                        elif cond(b, c) and c == n - 1:
                            inner_count += 1
                            if inner_count > count:
                                count = inner_count
                            c += 1
                        elif not cond(b, c) and c == n - 1:
                            b -= 1
                        elif not cond(b, c):
                            b += 1
                        else:
                            c += 1
                    b += 1
                elif cond(a, b) and b == n - 1:
                    inner_count += 1
                    if count < inner_count:
                        count = inner_count
                    b += 1
                elif not cond(a, b):
                    b += 1
                else:
                    b += 1

        return count if count > 0 else -1

    def maximumJumps3(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def f(i):
            if i == n - 1:
                return 0
            max_jumps = -1
            for j in range(i + 1, n):
                if -target <= nums[j] - nums[i] <= target:
                    jumps = f(j) + 1
                    if jumps > 0:
                        max_jumps = max(max_jumps, jumps)
            return max_jumps

        return f(0)

    # Submission - Answer
    """
    class Solution:
        def maximumJumps(self, nums: List[int], target: int) -> int:
            dp = [-1] * len(nums)
            dp[0] = 0
    
            for i in range(1, len(nums)):
                for j in range(i - 1, -1, -1):
                    if -target <= nums[i] - nums[j] and nums[i] - nums[j] <= target:
                        if dp[j] > -1:
                            dp[i] = max(dp[i], dp[j] + 1)
    
            return dp[-1]
    """
    # The Whales
    """
    class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def f(i):
            if i == n-1:
                return 0
            max_jumps = -1
            for j in range(i+1, n):
                if -target <= nums[j] - nums[i] <= target:
                    jumps = f(j) + 1
                    if jumps > 0:
                        max_jumps = max(jumps, max_jumps)
            return max_jumps
        return f(0)
    """


if __name__ == "__main__":
    input = ([1, 3, 6, 4, 1, 2], 2)
    inp6 = ([1, 3, 0, -1, 0, 1, 5, 7, 1], 2)
    inp7 = ([1, 4, 6, 10, 9, 13, 25, 12], 3)
    inp2 = ([1, 3, 1, 4, 1, 6, 1, 7, 5], 2)
    inp3 = ([1, 3, 6, 4, 1, 2], 3)
    inp5 = ([1, 3, 6, 4, 1, 2], 0)
    inp4 = ([1, 0, 2], 1)
    inputest3 = ([0, 2, 1], 1)
    inptest = ([1, -1, -3, -4, -6, -7, -8], 2)
    inputest4 = ([0, 2, 1, 3], 1)
    inputtest5 = ([1, 2, 0, 3], 2)
    inptest2 = (
        [
            1151004,
            -368271873,
            -959137308,
            -363298760,
            860913529,
            875734893,
            653205161,
            -726919163,
            -107413863,
            -142574923,
            535616977,
            -527647589,
            -933518315,
            622674836,
            -626420393,
            718010621,
            443503514,
            324638485,
            303398068,
            404393712,
            -682845482,
            957378126,
            254180033,
            527664388,
            204099822,
            59043697,
            284163204,
            -18806397,
            54466771,
            218940186,
            122932328,
            -527134788,
            748489009,
            481143527,
            -91930114,
            650935932,
            49918996,
            838929409,
            298033606,
            135544915,
            -231923297,
            -564040431,
            -403686128,
            -779212295,
        ],
        1152175137,
    )

    S = Solution()
    print(S.maximumJumps3(*input))
    # print(S.maximumJumps(*inp2))
    # print(S.maximumJumps2(*inp3))
    # print(S.maximumJumps(*inp4))
    # print(S.maximumJumps2(*inp5))
    # print(S.maximumJumps2(*inp6))
    # print(S.maximumJumps(*inp7))
    # print(S.maximumJumps2(*inputtest5))
