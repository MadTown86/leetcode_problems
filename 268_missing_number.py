# https://leetcode.com/problems/missing-number/

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = [x for x in range(len(nums)+1)]
        while nums:
            arg = nums.pop()
            print(arg)
            if arg in l:
                l.remove(arg)
                print(l)

        return l[0]

if __name__ == '__main__':
    inp = [0, 1, 3]
    inp2 = [9,6,4,2,3,5,7,0,1]
    S = Solution()
    print(S.missingNumber(inp2))
