from typing import List

"""
https://leetcode.com/problems/contains-duplicate-ii/

Given an integer array nums and an integer k, return true if there are two distinct 
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

from collections import defaultdict

class Solution:

    # Time complexity issue
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        i = 0
        while i < len(nums)-1:
            for j in range(i+1, len(nums) if (i+k) > len(nums)-1 else i+k+1):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
            i += 1
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        C = defaultdict(list)
        for index, number in enumerate(nums):
            C[number] += [index]
        for l in C.values():
            if len(l) > 1:
                while l:
                    first = l.pop(0)
                    next = l[0] if l else 0
                    if abs(first-next) <= k:
                        return True
        return False

# https://leetcode.com/problems/contains-duplicate-ii/discuss/2463150/Very-Easy-oror-100-oror-Fully-Explained-oror-Java-C%2B%2B-Python-Javascript-Python3-(Using-HashSet)
# Other Answer on Leetcode

"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create hset for storing previous of k elements...
        hset = {}
        # Traverse for all elements of the given array in a for loop...
        for idx in range(len(nums)):
            # If duplicate element is present at distance less than equal to k, return true...
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True
            hset[nums[idx]] = idx
        # If no duplicate element is found then return false...
        return False
"""



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

    # S.contains2(e)

