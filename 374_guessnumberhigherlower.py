# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
class Solution:
    def guessNumber(self, n: int) -> int:
        high = n
        low = 1
        mid = high // 2
        while True:
            if high - low == 0:
                return low
            if high - low == 1:
                if guess(high) == 0:
                    return high
                if guess(low) == 0:
                    return low
            resp = guess(mid)
            if resp == -1:
                high = mid
                mid = (high - low) // 2
            elif resp == 1:
                low = mid
                mid = ((high - low) // 2) + low
            elif resp == 0:
                return mid


if __name__ == "__main__":
    S = Solution()
    S.guessNumber(10)