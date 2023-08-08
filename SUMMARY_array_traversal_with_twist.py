# https://leetcode.com/problems/jump-game-ii/description/


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        crap = []

        @cache
        def f(i):
            if i == n - 1:
                return 0
            min_jumps = n - 1

            print(abs(n - (nums[i] + 1)))
            for j in (i + 1, i + nums[i]):
                jumps = f(j) + 1
                if jumps > 0:
                    min_jumps = min(min_jumps, jumps)
            return min_jumps

        # print(crap)
        return f(0)

    # https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

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
