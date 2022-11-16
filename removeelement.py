"""
https://leetcode.com/problems/remove-element/
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        k = 0
        flag = False  # One of val found
        valflag = False
        # If all values dont' have val
        # If all values are val
        # If no values
        # If 1 value is val
        # IF 1 value is not val
        # If mixed values with repeats

        # Outlier case empty list
        if len(nums) == 0:
            return 0

        # Outlier Case - single sized
        if i == j and nums[i] != val:
            return 1
        elif i == j and nums[i] == val:
            return 0

        while i != j and len(nums) > 2:
            if nums[i] != val:
                i += 1
                # Case where no values because j didn't move
                if i + 1 == j and j == len(nums)-1:
                    if nums[i] != val:
                        return len(nums)-1
                elif i + 1 == j and nums[j] == val:
                    return i
                elif i + 1 == j and nums[j] != val:
                    return j
            elif nums[i] == val:
                flag = True
                if nums[j] != val:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    while nums[j] == val and j != i:
                        j -= 1
                    if (j-1) != i:
                        nums[i], nums[j] = nums[j], nums[i]
                    elif j - 1 == i and i == 0:
                        # This case should funnel down to initial i == val and J steppin down to be one away
                        return 0

        return i




if __name__ == "__main__":
    test = [3, 2, 2, 3]
    test2 = [0, 1, 2, 2, 3, 0, 4, 2]
    test3 = [3, 3]
    test4 = [4, 5]
    test5 = [4, 5]
    test6 = [2, 2, 2]
    s = Solution()
    print(s.removeElement(test2, 2))
