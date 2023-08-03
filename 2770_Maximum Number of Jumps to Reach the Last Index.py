# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        count_max = 0
        def traverse(nums, target, count):
            nonlocal count_max
            if len(nums) == 1:
                if count > count_max:
                    count_max = count
            for x in range(1, len(nums)):
                if -target <= nums[x] - nums[0] <= target:
                    traverse(nums[x:], target, count + 1)
                if x == len(nums)-1 and -target <= nums[x] - nums[0] <= target:
                    count += 1
                    if count > count_max:
                        count_max = count

        traverse(nums, target, 0)
        return count_max if count_max > 0 else -1

    def maximumJumps2(self, nums: List[int], target: int) -> int:
        a, b = 0, 1
        n = len(nums)

        pos_one_moves = []
        count = 0

        while b < n-1:
            if -target <= nums[b] - nums[a] <= target:
                pos_one_moves.append(b)
                b += 1
            b += 1

        a, b = 0, 1

        while a <= len(pos_one_moves)-1:
            interim_count = 0 + a
            while b <= n-1:
                if -target <= nums[b] - nums[pos_one_moves[a]] <= target:
                    interim_count += 1
                    b += 1
                b += 1
            if count < interim_count:
                count = interim_count
            a += 1

        return count if count > 0 else -1








if __name__ == "__main__":
    input = ([1, 3, 6, 4, 1, 2], 2)
    inp6 = ([1, 3, 0, -1, 0, 1], 2)
    inp7 = ([1, 4, 6, 10, 9, 13, 25, 12], 3)
    inp2 = ([1, 3, 1, 4, 1, 6, 1, 7, 5], 2)
    inp3 = ([1, 3, 6, 4, 1, 2], 3)
    inp5 = ([1, 3, 6, 4, 1, 2], 0)
    inp4 = ([1, 0, 2], 1)
    inptest = ([1, -1, -3, -4, -6, -7, -8], 2)
    inptest2 = ([1151004,-368271873,-959137308,-363298760,860913529,875734893,653205161,-726919163,-107413863,-142574923,535616977,-527647589,-933518315,622674836,-626420393,718010621,443503514,324638485,303398068,404393712,-682845482,957378126,254180033,527664388,204099822,59043697,284163204,-18806397,54466771,218940186,122932328,-527134788,748489009,481143527,-91930114,650935932,49918996,838929409,298033606,135544915,-231923297,-564040431,-403686128,-779212295], 1152175137)

    S = Solution()
    print(S.maximumJumps2(*input))
    # print(S.maximumJumps(*inp2))
    # print(S.maximumJumps(*inp3))
    # print(S.maximumJumps(*inp4))
    # print(S.maximumJumps(*inp5))
    # print(S.maximumJumps(*inp6))
    # print(S.maximumJumps(*inp7))
    # print(S.maximumJumps2(*inptest2))


