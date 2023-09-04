# This is just practice creating an algorithm to make all permutations of an array
from typing import List
from itertools import combinations


def permutation_array(nums: List[int]) -> List[List[int]]:
    i, n = 0, len(nums)
    res = []
    while i < n:
        b = i + 1
        permutation = []
        offset = 0
        while offset < n - i:
            bo = b + offset
            bo_list = [nums[i]]
            while bo < n:
                bo_list.append(nums[bo])
                bo += 1
            permutation.append(bo_list)
            offset += 1
        if permutation:
            res.append(permutation)
        i += 1

    return res


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for permutation in permutation_array(nums):
        print(permutation)

    print(combinations(nums))
