from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x, count = 0, 0
        while x < len(nums) and count < len(nums) - 1:
            if nums[x] == 0:
                zero = nums.pop(x)
                nums.append(zero)
            if nums[x] != 0:
                x += 1
            count += 1
        print(nums)

if __name__ == "__main__":
    S = Solution()
    inps = [[0]]
    for arg in inps:
        S.moveZeroes(arg)

