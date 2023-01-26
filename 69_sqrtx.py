class Solution:
    def mySqrt(self, x: int) -> int:
        b = 1
        count = 1
        while x:
            x = x - b
            b += 2

        return count

if __name__ == "__main__":
    args = [4, 8]
    S = Solution()
    for arg in args:
        print(S.mySqrt(arg))

