# https://leetcode.com/problems/single-number/

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for item in nums:
            if nums.count(item) != 2:
                return item
            else:
                continue

    def singleNumber2(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return nums[0]
        if len(nums) == 3:
            nums.sort()
            return nums[0] if nums[0] != nums[1] else nums[2]
        else:
            nums.sort()
            print(nums)
            x, y = 0, 1
            while y <= len(nums)-1:
                print(x, y)
                if nums[x] != nums[y] and y < len(nums) - 1:
                    return nums[x]
                elif nums[x] != nums[y] and y == len(nums) - 1:
                    return nums[y]
                else:
                    x += 2
                    y += 2
            return nums[-1]

"""
Answers from LeetCode
def singleNumber(self, nums):
    for i in range(1,len(nums)):
        nums[0] ^= nums[i]
    return nums[0]
    
    
def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key

def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res
    
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)
    
def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)
    
def singleNumber(self, nums):
    return reduce(operator.xor, nums)
"""
if __name__ == "__main__":
    n = [4, 1, 2, 1, 2]
    S = Solution()
    print(S.singleNumber2(n))