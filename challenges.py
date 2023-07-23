
class Solution2:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (2*t)

from typing import List

class Solution:
    paths = []
    counter = 0
    def maximumJumps(self, nums: List[int], target: int) -> int:
        S.paths = []
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
        true_cond = lambda: print(f'TRUE: {i}>>{j} :: {-target} <= {nums[j]} - {nums[i]} <= {target}')
        false_cond = lambda: print(f'FALSE: {i}>>{j} :: {-target} <= {nums[j]} - {nums[i]} <= {target}')
        condition = lambda i, j, target: -target <= nums[j]-nums[i] <= target
        flag = False

        def optional_paths(i_pos: int, nums: List[int], target: int) -> List[int]:
            self.counter += 1
            res = []
            j = i_pos + 1
            while j < len(nums):
                if condition(i_pos, j, target):
                    true_cond()
                    res.append(j)
                    j += 1
                else:
                    false_cond()
                    j += 1
            return res
        path_list = optional_paths(i, nums, target)

        print(f'path_list: {path_list}')

        def traverse(single_path) -> int:
            for x in optional_paths(single_path, nums, target):
                traverse(x)

        while path_list:
            self.counter = 0
            single_path = path_list.pop()
            traverse(single_path)
            self.paths.append(self.counter)

        return max(self.paths)












if __name__ == "__main__":
    input = ([1, 3, 6, 4, 1, 2], 2)
    inp2 = ([1, 3, 1, 4, 1, 6, 1, 7, 8], 2)
    inp3 = ([1, 3, 6, 4, 1, 2], 3)
    inp4 = ([1, 0, 2], 1)

    S = Solution()
    print(S.maximumJumps(*input))
    print(S.maximumJumps(*inp2))
    print(S.maximumJumps(*inp3))
    print(S.maximumJumps(*inp4))


