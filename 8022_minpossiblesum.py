class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        position = 0
        additional_value = 1
        dynamic_target = 0
        summed = 0
        blocked = []
        nums = []
        while position < n:
            if additional_value <= target // 2:
                summed += additional_value
                additional_value += 1
                position += 1
            elif additional_value < target and additional_value > target // 2:
                additional_value += 1
            else:
                summed += additional_value
                additional_value += 1
                position += 1
        return summed




if __name__ == "__main__":
    """
        Is beautiful
        nums.length == n
        nums consists of pairwise distinct positive integers
        There doesn'te xist two distinct indices, i and j, in the range [0, n-1], such that nums[i] + nums[j] == target
    """
    inputs = [[2, 3], [3, 3], [1, 1], [4, 4]]
    S = Solution()

    # assert S.minimumPossibleSum(*inputs[0]) == 4
    # assert S.minimumPossibleSum(*inputs[1]) == 8
    # assert S.minimumPossibleSum(*inputs[2]) == 1
    assert S.minimumPossibleSum(16, 6) == 162
    # S.minimumPossibleSum(*inputs[3])
