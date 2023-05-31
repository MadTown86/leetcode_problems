# https://leetcode.com/problems/summary-ranges/
# *sigh*
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        a = 0
        b = 0
        count = 0
        while b+1 <= len(nums)-1:
            if nums[a + count] != nums[b + count + 1]+1 and a == b:
                res.append(str(nums[a]))
                a += 1
                b += 1
            elif nums[a + count] != nums[b+count+1] +1 and a != b:
                res.append(str(nums[a]) + '->' + str(nums[b+count]))
                a = b + count
                b = b + count
            elif nums[a + count] == nums[b+count + 1]+1 and a != b:
                count += 1
            elif nums[a] == nums[b+1]+1:
                b += 1



        return res

if __name__ == '__main__':
    inp1 = [0, 5, 6, 10, 11, 12, 14, 16, 17, 18, 90]
    S = Solution()
    print(S.summaryRanges(inp1))
