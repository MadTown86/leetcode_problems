class Solution2:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (2*t)

from typing import List

class Solution:
    paths = []
    def maximumJumps(self, nums: List[int], target: int) -> int:
        """
        Step through the list and find the maximum amount of 'jumps' that can be made while conforming to
        certain conditions.
        Step forward condition:
        0 <= i < j < n

        Step Calc Condition:
        -terget <= nums[j]-nums[i] <= target

        """
        i, iss, j, n = 0, 0, 1, len(nums)
        valid_moves_bin = {}
        valid_tries = []
        condition = lambda i, j, target: -target <= nums[j]-nums[i] <= target
        flag = False

        for i in range(iss, n):
            temp = []
            j = i + 1
            while j < n:
                if condition(i, j, target):
                    print(f'TRUE: {i}>>{j} :: {-target} <= {nums[j]} - {nums[i]} <= {target}')
                    temp.append(j)
                    j += 1
                else:
                    print(f'FALSE: {i}>>{j} :: {-target} <= {nums[j]} - {nums[i]} <= {target}')
                    j += 1
            valid_moves_bin[i] = temp

        for key in valid_moves_bin.keys():
            while valid_moves_bin[key]:








if __name__ == "__main__":
    input = ([1, 3, 6, 4, 1, 2], 2)
    inp2 = ([1, 3, 1, 4, 1, 6, 1, 7, 8], 2)
    inp3 = ([1, 3, 6, 4, 1, 2], 3)
    inp4 = ([1, 0, 2], 1)

    S = Solution()
    print(S.maximumJumps(*input))
    # print(S.maximumJumps(*inp2))
    # print(S.maximumJumps(*inp3))
    # print(S.maximumJumps(*inp4))


