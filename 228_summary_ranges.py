# https://leetcode.com/problems/summary-ranges/
# *sigh*
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []  # Result array
        a = 0  # Lagging position
        b = 0  # Stepping position

        # Loop condition met until 'second' condition would otherwise break
        while (b+1) <= len(nums)-1:

            # Turning conditionals into variables to reduce typing
            first = nums[a + (b-a)] + 1
            second = nums[b + 1]

            # print('__________BEGIN_________')
            # print(f'FIRST : {first} --- SECOND: {second}')
            # print(f'A: {a} --- B: {b}')
            # print(f'RES: {res}')
            # print('________________________')

            # Step b if follows incremental pattern
            if first == second:
                b += 1

            # Adds single position when solo range
            if first != second and a == b and b != len(nums)-1:
                res.append(str(nums[a]))
                a += 1
                b += 1

            # Adds a range to res when end of range found
            if first != second and a != b:
                res.append(str(nums[a]) + '->' + str(nums[b]))
                a = b+1
                b = b+1

            # End case check with solo range at last index position
            if a == b and b == len(nums)-1 and nums[a-1] != nums[b]+1:
                res.append(str(nums[b]))

            # End case check with multi range at last index position
            if a != b and b == len(nums)-1 and nums[a] + 1 == nums[b]:
                res.append(str(nums[a]) + '->' + str(nums[b]))

            # print('__________END_________')
            # print(f'FIRST : {first} --- SECOND: {second}')
            # print(f'A: {a} --- B: {b}')
            # print(f'RES: {res}')
            # print('________________________')

        return res

if __name__ == '__main__':
    inp1 = [0, 5, 6, 10, 11, 12, 14, 16, 17, 18, 90]
    inp2 = [0, 1, 2, 4, 5, 7]
    inp3 = [0, 2, 3, 4, 6, 8, 9]
    S = Solution()
    print(S.summaryRanges(inp3))
