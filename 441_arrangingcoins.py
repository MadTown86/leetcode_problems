# https://leetcode.com/problems/arranging-coins/
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        flights = 0
        if n < 4:
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n == 3:
                return 2
        cursor = 0
        counter = 1
        while cursor <= n:
            cursor += counter
            counter += 1
            if cursor <= n:
                flights += 1
            print(f'{cursor=}, {counter=}, {flights=}')

        return flights

# Better Solution
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left,right=1,n
        while left<=right:
            mid=(right+left)//2
            num=(mid/2)*(mid+1)
            if num<=n:
                left=mid+1
            else:
                right=mid-1
        return right
"""




if __name__ == "__main__":
    S = Solution()
    inp = 20
    print(S.arrangeCoins(inp))
