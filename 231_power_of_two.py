#  https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n % 1 != 0:
            return False
        if n == 1:
            return True
        return self.isPowerOfTwo(n / 2)

if __name__ == '__main__':
    S = Solution()
    inp1 = 1
    print(S.isPowerOfTwo(inp1))