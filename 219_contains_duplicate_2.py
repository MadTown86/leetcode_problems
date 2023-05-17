from typing import List

"""
https://leetcode.com/problems/contains-duplicate-ii/

Given an integer array nums and an integer k, return true if there are two distinct 
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dammit Muumi, why are you so smart.
        print(f'NUMS: {nums}')
        for x in range(len(nums) - k if k < len(nums) else len(nums)):
            print(f'X: {x}')
            y = x + 1
            while y <= x+k and y <= len(nums)-1:
                print(f'Y: {y}')
                if nums[x] == nums[y]:
                    return True
                y += 1
        return False



if __name__ == "__main__":
    S = Solution()
    a = [1, 2, 3, 1]
    b = [1, 0, 1, 1]
    c = [1, 2, 3, 1, 2, 3]
    d = [99, 99]
    e = [1,2,3,4,5,6,7,8,9,9]
    # S.containsNearbyDuplicate(e, 3)
    # S.containsNearbyDuplicate(a, 3)
    # S.containsNearbyDuplicate(b, 1)
    # S.containsNearbyDuplicate(c, 2)

    assert S.containsNearbyDuplicate(a, 3) is True
    assert S.containsNearbyDuplicate(b, 1) is True
    assert S.containsNearbyDuplicate(c, 2) is False
    assert S.containsNearbyDuplicate(d, 2) is True
    assert S.containsNearbyDuplicate(e, 3) is True

