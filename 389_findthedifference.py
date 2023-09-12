# https://leetcode.com/problems/find-the-difference/

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(s)
        d = Counter(t)

        for x in d.keys():
            if x not in c.keys():
                return x
            elif d[x] != c[x]:
                return x


if __name__ == "__main__":
    S = Solution()
    inp = [("abcd", "abcde"), ("", "y"), ("a", "aa")]

    assert S.findTheDifference(*inp[0]) == "e"
    assert S.findTheDifference(*inp[1]) == "y"
    assert S.findTheDifference(*inp[2]) == "a"
