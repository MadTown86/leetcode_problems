# https://leetcode.com/problems/binary-search/

from typing import List
class Solution:
    def search2(self, nums: List[int], target: int) -> int:
        fp, mid, sp = 0, len(nums) // 2, len(nums)-1
        if len(nums) == 1:
            if nums[0] != target:
                return -1
            else:
                return 0
        while nums[mid] != target:
            if sp-fp <= 3:
                for ind in range(fp, sp+1):
                    if nums[ind] == target:
                        return ind
                return -1
            if target > nums[mid]:
                fp = mid
                mid = ((sp - fp) // 2) + fp
            if target < nums[mid]:
                fp = 0
                sp = mid
                mid = (sp - fp) // 2
        return mid

    def search(self, nums: List[int], target: int)->int:
        s, e = 0, len(nums)-1
        m = (e - s) // 2
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        while nums[m] != target:
            if e-s == 1:
                if nums[e] == target:
                    return e
                if nums[s] == target:
                    return s
                else:
                    return -1
            if nums[m] > target:
                e = m
                m = (e-s) // 2
            elif nums[m] < target:
                s = m
                m = ((e-s)//2) + s
        return m



if __name__ == "__main__":
    S = Solution()
    inp = [([1, 1], 0), ([1, 2, 3], 1), ([1, 2, 3], 3), ([0, 1], 1), ([0, 1], 0), ([-1, 0, 3, 5, 9, 12], 2), ([1, 2, 3, 4], 3), ([1, 2, 3, 4, 5], 4),
           ([1, 2, 3, 4, 5], 1), ([1, 2, 3, 4, 5], 5), ([1, 2, 3, 4], 4), ([1, 2, 3, 4], 1), ([-1,0,3,5,9,12], 3) ]

    assert S.search(*inp[0]) == -1
    assert S.search(*inp[1]) == 0
    assert S.search(*inp[2]) == 2
    assert S.search(*inp[3]) == 1
    assert S.search(*inp[4]) == 0
    # assert S.search(*inp[5]) == 4
    # assert S.search(*inp[6]) == 3
    # assert S.search(*inp[7]) == 0
    # assert S.search(*inp[8]) == 2
