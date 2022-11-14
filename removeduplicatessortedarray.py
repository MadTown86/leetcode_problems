"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
"""

# First Solution but slower beat 60% on memory though
class Solution:
    def removeDuplicates(self, n: list) -> int:
        i = 0
        j = 1
        while j < len(n) and n[j] >= n[i]:
            if n[i] == n[j]:
                n.pop(j)
            else:
                i += 1
                j += 1

        return len(n)

# This answer was sufficient, increased speed but also increased memory usage
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        i, j = 0, 1
        lastval = 0
        duplicatecount = 0
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[i] == nums[j]:
                return 1
            else:
                return 2
        while j < len(nums):
            if nums[i] == nums[j]:
                lastval = nums[i]
                duplicatecount += 1
                nums[j] = None
                i += 1
                j += 1
            elif nums[i] == None and nums[j] != None and nums[j] == lastval:
                nums[j] = None
                duplicatecount += 1
                j += 1
            elif nums[i] == None and nums[j] != None and nums[j] > lastval:
                nums[i] = nums[j]
                lastval = nums[i]
                nums[j] = None
                i += 1
                j += 1
            else:
                i += 1
                j += 1
        if duplicatecount == 0:
            return len(nums)
        else:
            return i

# Worse on time but a little better on memory
class Solution:
    def removeDuplicates(self, n: list) -> int:
        i = 0
        j = 1
        if len(n) == 2:
            if n[i] == n[j]:
                return 1
            else:
                return 2
        while j < len(n)-1:
            if n[i] == n[j]:
                j += 1
            if n[i] != n[j]:
                n[i+1] = n[j]
                i += 1
        return i + 1

#Good Leetcode Answer:
#I should have better taken into account that I didn't have to ever compare values as greater/less than, which may
#cost more.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        j = 0
        while j < len(nums) :
            if nums[i] == nums[j]:
                j += 1
            elif nums[i] != nums[j]:
                i+= 1
                nums[i] , nums[j] = nums[j] , nums[i]
                j+= 1
        return i+1
"""

#I don't know why I didn't think of the whole switcharoo instead of the re-write.  This is what shortens the load

#01N1122334
#1N1

test = [1, 2, 3, 4]

test1 = [0,0,1,1,1,2,2,3,3,4]



test2 = [1, 1, 2]

s = Solution()
print(s.removeDuplicates(test))
