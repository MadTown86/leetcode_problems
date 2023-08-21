# https://leetcode.com/problems/jump-game-ii/description/
from typing import List
from functools import cache


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

    def jump2(self, nums: List[int]) -> int:
        start, n = 0, len(nums)
        stack = [list(range(start+1, start + nums[start]+1))]
        count = 0
        count_stack = []
        print(stack)
        while stack:
            depth_level = stack.pop()
            print(f'{depth_level=}')
            count += 1
            add_container = []
            for x in depth_level:
                if isinstance(x, int):
                    end_range = x + nums[x] + 1
                    print(f'{x=} :: {depth_level=} :: {end_range=}')
                    if end_range > n:
                        count_stack.append(count)
                        end_range = n-1
                    add_container.append(list(range(x+1, end_range)))
                if isinstance(x, list):
                    for y in x:
                        end_range2 = y + nums[y] + 1
                        if end_range2 > n:
                            count_stack.append(count)
                            end_range2 = n-1
                        add_container.append(list(range(y+1, end_range2)))
            if add_container:
                stack.append(add_container)

        print(f'{count_stack=}')

    def jump3(self, nums: List[int]) -> int:
        start, n = 0, len(nums)
        stack = [list(range(start + 1, start + nums[start] + 1))]
        count = 0
        count_stack = []
        print(stack)
        while stack:
            depth_level = stack.pop()
            print(f'{depth_level=}')
            count += 1
            add_container = []

            for x in depth_level:
                range_builder = []
                if isinstance(x, int):
                    step = x + 1
                    end_range = x + nums[x] + 1
                    if end_range >= n:
                        count_stack.append(count)
                        end_range = n-1
                    while step < end_range:
                        range_builder.append(step)
                        step += 1
                if isinstance(x, list):
                    for y in x:
                        step2 = y + 1
                        end_range = y + nums[y] + 1
                        if end_range >= n:
                            count_stack.append(count)
                            end_range = n-1
                        while step2 < end_range:
                            range_builder.append(step2)
                            step2 += 1
                add_container.append(range_builder)



            if add_container:
                stack.append(add_container)

        print(f'{count_stack=}')








if __name__ == "__main__":
    S = Solution()
    inputs = [[2, 3, 1, 1, 4], [2, 3, 0, 1, 4], [4, 1, 1, 1, 1]]

    for x in inputs:
        S.jump3(x)
