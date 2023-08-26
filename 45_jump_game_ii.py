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
        stack = [list(range(start + 1, start + nums[start] + 1))]
        count = 0
        count_stack = []
        print(stack)
        while stack:
            depth_level = stack.pop()
            print(f"{depth_level=}")
            count += 1
            add_container = []
            for x in depth_level:
                if isinstance(x, int):
                    end_range = x + nums[x] + 1
                    print(f"{x=} :: {depth_level=} :: {end_range=}")
                    if end_range > n:
                        count_stack.append(count)
                        end_range = n - 1
                    add_container.append(list(range(x + 1, end_range)))
                if isinstance(x, list):
                    for y in x:
                        end_range2 = y + nums[y] + 1
                        if end_range2 > n:
                            count_stack.append(count)
                            end_range2 = n - 1
                        add_container.append(list(range(y + 1, end_range2)))
            if add_container:
                stack.append(add_container)

        print(f"{count_stack=}")

    def jump3(self, nums: List[int]) -> int:
        start, n = 0, len(nums)
        run = 1
        last_start, last_end = 0, 0
        stack = [(run, start + 1, start + nums[start])]
        count_stack = []
        if n == 1:
            return 0
        if nums[start] + start >= n - 1 and nums[start] != 0:
            return 1
        while stack:
            if len(stack[0]) == 3:
                run, begin, stop = stack.pop(0)
            else:
                run, begin = stack.pop(0)
                stop = begin
            if count_stack and run > min(count_stack):
                break
            run += 1
            while begin <= stop and begin < n:
                if nums[begin] == 0:
                    begin += 1
                if begin >= n - 1:
                    break
                if nums[begin] < stop - begin:
                    begin += 1
                start = begin + 1
                end = begin + nums[begin]
                # print(f"{stack=}::{current=}::{index=}::{start=}::{end=}")
                if end >= n - 1:
                    count_stack.append(run)
                else:
                    if last_end > end and last_start > start:
                        begin += 1
                    else:
                        if stack:
                            stack.pop()
                        if start == end and end < n:
                            stack.append((run, start))
                        else:
                            last_start = start
                            last_end = end
                            stack.append((run, start, end))
                begin += 1
            # print(f"{count_stack=}")

        return min(count_stack) if count_stack else 0

    def jump4(self, nums: List[int]) -> int:
        n = len(nums)
        cursor = 0
        steps = 0
        while cursor < n - 1:
            longest_jump = -nums[cursor]
            increment = nums[cursor]
            s = cursor + 1
            end = cursor + increment
            if end >= n - 1:
                steps += 1
                break
            jump_point = 0
            while s <= end:
                if nums[s] - (end - s) > longest_jump:
                    longest_jump = nums[s] - (end - s)
                    jump_point = s
                    s += 1
                else:
                    s += 1
            if jump_point == 0:
                return 0
            cursor = jump_point
            steps += 1
        return steps


if __name__ == "__main__":
    S = Solution()
    inputs = [
        [2, 3, 1, 1, 4],
        [2, 3, 0, 1, 4],
        [4, 1, 1, 1, 1],
        [1, 0, 0],
        [3, 1, 1, 4, 1, 5, 1, 1, 1, 1],
        [3, 2, 1],
        [2, 3, 1],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0],
        [0],
        [1],
        [2, 1],
        [1, 2],
        [1, 2, 1, 1, 1],
        [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0],
        [2, 1, 1, 1, 1],
        [
            5,
            6,
            4,
            4,
            6,
            9,
            4,
            4,
            7,
            4,
            4,
            8,
            2,
            6,
            8,
            1,
            5,
            9,
            6,
            5,
            2,
            7,
            9,
            7,
            9,
            6,
            9,
            4,
            1,
            6,
            8,
            8,
            4,
            4,
            2,
            0,
            3,
            8,
            5,
        ],
        [
            8,
            2,
            4,
            4,
            4,
            9,
            5,
            2,
            5,
            8,
            8,
            0,
            8,
            6,
            9,
            1,
            1,
            6,
            3,
            5,
            1,
            2,
            6,
            6,
            0,
            4,
            8,
            6,
            0,
            3,
            2,
            8,
            7,
            6,
            5,
            1,
            7,
            0,
            3,
            4,
            8,
            3,
            5,
            9,
            0,
            4,
            0,
            1,
            0,
            5,
            9,
            2,
            0,
            7,
            0,
            2,
            1,
            0,
            8,
            2,
            5,
            1,
            2,
            3,
            9,
            7,
            4,
            7,
            0,
            0,
            1,
            8,
            5,
            6,
            7,
            5,
            1,
            9,
            9,
            3,
            5,
            0,
            7,
            5,
        ],
    ]

    for x in inputs:
        print(S.jump4(x))
