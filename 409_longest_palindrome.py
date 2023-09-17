# https://leetcode.com/problems/longest-palindrome/
from collections import defaultdict


class Solution:
    def longestPalindrome2(self, s: str) -> int:
        """
        Good Answer but don't need to actually build the palindrome.  So going to refactor
        """
        d = defaultdict(int)
        for x in s:
            d[x] += 1
        f, m, b = "", "", ""
        d_copy = d.copy()
        odd = {}
        for x, y in d.items():
            if y % 2 == 0:
                f = (x * (y // 2)) + f
                b += x * (y // 2)
            else:
                odd[x] = y
                d_copy.pop(x)

        if len(odd.keys()) <= 1:
            for x, y in odd.items():
                m += x * y

        elif odd:
            first = [x for x in odd.keys()][0]
            for x, y in odd.items():
                if odd[first] < y:
                    first = x
            m += first * odd[first]
            odd.pop(first)

            for x, y in odd.items():
                if y > 2:
                    odd_toeven = y - 1
                    count = odd_toeven // 2
                    f = count * x + f
                    b += count * x

        return len(f + m + b)

    def longestPalindrome(self, s: str) -> int:
        count = 0
        d = defaultdict(int)
        for x in s:
            d[x] += 1

        odd = {}
        for x, y in d.items():
            if y % 2 == 0:
                count += y
            else:
                odd[x] = y

        if len(odd.keys()) <= 1:
            for x, y in odd.items():
                count += y

        elif odd:
            first = [x for x in odd.keys()][0]
            for x, y in odd.items():
                if odd[first] < y:
                    first = x
            count += odd[first]
            odd.pop(first)

            for x, y in odd.items():
                if y > 2:
                    count += y - 1

        return count


if __name__ == "__main__":
    S = Solution()
    inp = [
        "abccccdd",
        "a",
        "abbacddeeef",
        "ccc",
        "ababababa",
        "zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez",
    ]
    assert S.longestPalindrome(inp[0]) == 7
    assert S.longestPalindrome(inp[1]) == 1
    assert S.longestPalindrome(inp[2]) == 9
    assert S.longestPalindrome(inp[3]) == 3
    assert S.longestPalindrome(inp[4]) == 9
    assert S.longestPalindrome(inp[5]) == 55

    # print(S.longestPalindrome(inp[5]))
