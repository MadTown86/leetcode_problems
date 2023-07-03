# https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            arg = n / 2
            return self.isUgly(int(arg))
        elif n % 3 == 0:
            arg = n / 3
            return self.isUgly(int(arg))
        elif n % 5 == 0:
            arg = n / 5
            return self.isUgly(int(arg))
        return False


if __name__ == '__main__':
    S = Solution()
    args = [6, 1, 14]
    for arg in args:
        print(S.isUgly(arg))