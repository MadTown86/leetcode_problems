"""
https://leetcode.com/problems/remove-element/
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        c = 0

        # Outlier case empty list
        if len(nums) == 0:
            return 0

        # Outlier Case - single sized
        if i == j and nums[i] != val and len(nums) == 1:
            return 1
        elif i == j and nums[i] == val:
            return 0

        # Outlier Case - len == 2
        if len(nums) == 2:
            if nums.count(val) == 0:
                return len(nums)
            elif nums.count(val) == 2:
                return 0
            elif nums[0] == val:
                nums[0], nums[1] = nums[1], nums[0]
                nums[1] = '_'
                return 1
            else:
                return 1

        # All positions = val
        if nums.count(val) == len(nums):
            for i in range(len(nums)):
                nums[i] = '_'
            return 0

        if nums.count(val) == 0:
            return len(nums)


        # Situation [2, 2, 3] val = 2
        # All cases that reach this point will be >= three in length and not be
        while True:
            # I want to try the paradigm of counterexample - only checking for negatives not confirming postiives
            if i + 1 == j:
                if nums[i] == val:
                    nums[i] = '_'
                    nums[i], nums[j] = nums[j], nums[i]
                    c += 1
                    return len(nums) - c
                else:
                    if nums[j] == val:
                        nums[j] = '_'
                        c += 1
                    return len(nums) - c
            elif nums[i] == val:
                if nums[j] == val:
                    if nums[j] == '_':
                        j -= 1
                    else:
                        nums[j] = '_'
                        c += 1
                        j -= 1
                elif nums[j] != val:
                    nums[i] = '_'
                    c += 1
                    nums[i], nums[j], = nums[j], nums[i]

            else:
                i += 1







if __name__ == "__main__":


    test = ([3, 2, 2, 3], 3)
    test2 = [0, 1, 2, 2, 3, 0, 4, 2]
    test3 = ([3, 3], 0)
    test4 = ([4, 5], 4)
    test5 = ([4, 5], 5)
    test6 = ([2, 2, 2], 2)
    test7 = ([2, 2, 3], 3)
    test8 = [2, 2, 3]
    test9 = [1, 2, 3, 4]
    test10 = [0, 1, 2, 2, 3, 0, 4, 2]
    testbin = [test, test2, test3, test4, test5, test6, test7]

    s = Solution()


    print(s.removeElement(test2, 2))
