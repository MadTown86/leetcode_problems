# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(arg):
    if arg >= 1702766719:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        print(f'n: {n}')
        mid = n // 2
        print(f'mid {mid}')
        while True:
            if not isBadVersion(mid):
                mid = ((n - mid) // 2) + mid




if __name__ == '__main__':
    """
    2126753390
    1702766719
    """
    inp = 2126753390
    S = Solution()
    print(f'RESULT: {S.firstBadVersion(inp)}')