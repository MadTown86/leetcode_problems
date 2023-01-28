from math import floor
class Solution:
    # Had to look up a mathematical approach with powers/math functions not allowed
    # newton raphson method sqrt
    # At least learned a mathematical appraoch to obtaining the square root.
    def mySqrt(self, x: int) -> int:
        n = x
        t = .00001
        if x == 0:
            return 0
        while True:
            root = .5 * (n + (x / n))
            if (abs(root-n) < t):
                break
            n = root

        return floor(root)





if __name__ == "__main__":
    args = [1, 0, 4, 8, 3, 13, 5, 75, 112, 1212]
    S = Solution()
    for arg in args:
        print(S.mySqrt(arg))

