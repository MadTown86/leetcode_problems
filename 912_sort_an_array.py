from typing import List

# https://leetcode.com/problems/sort-an-array/
# https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7
# I was able to get help looking at a version of mergesort pattern.

# speed/time req's - O(nlog(n))

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def recurseit(nums):
            if len(nums) <= 1:
                return

            mid = len(nums) // 2
            left_end = nums[:mid]
            right_end = nums[mid:]

            left_index = 0
            right_index = 0
            base_index = 0

            recurseit(left_end)
            recurseit(right_end)

            while left_index < len(left_end) and right_index < len(right_end):
                if left_end[left_index] < right_end[right_index]:
                    nums[base_index] = left_end[left_index]
                    left_index += 1
                else:
                    nums[base_index] = right_end[right_index]
                    right_index += 1
                base_index += 1

            if left_index < len(left_end):
                del nums[base_index:]
                nums += left_end[left_index:]
            if right_index < len(right_end):
                del nums[base_index:]
                nums += right_end[right_index:]

        recurseit(nums)
        return nums






if __name__ == "__main__":
    l = [5, 2, 3, 6, 7, 8, 9, 2, 5, 9, 10, 25, 18, 32, 44, 54, 99, 32, 1, 0]
    S = Solution()
    S.sortArray(l)
    print(l)




