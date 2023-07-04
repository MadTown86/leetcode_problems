# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(arg):
    if arg >= 1:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        mid = n // 2
        while True:
            print(f' N: {n}, mid: {mid}')
            if not isBadVersion(mid):
                r = n - mid
                if n - mid <= 1:
                    return n
                mid = ((r) // 2) + mid
                print(f'MID1: {mid}')
            elif isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid):
                n = mid
                mid = n // 2
                if mid <= 1:
                    if isBadVersion(1):
                        return 1
                print(f'MID2: {mid}')


if __name__ == '__main__':
    """
    2126753390
    1702766719
    """
    inp = 10
    S = Solution()
    print(f'RESULT: {S.firstBadVersion(inp)}')