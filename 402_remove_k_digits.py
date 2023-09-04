# https://leetcode.com/problems/remove-k-digits/description/

import math


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        res, front = num[k:], num[:k]
        b = 0
        while front:
            digit = front[0]
            if digit <= min(front) and digit < res[b]:
                res = res[:b] + digit + res[b + 1 :]
                front = front[1:]
                b += 1
            elif digit > min(front):
                front = front[1:]
            elif digit <= min(front) and digit > res[b]:
                front = front[1:]
                b += 1
            elif digit <= min(front) and digit < res[b]:
                front = front[1:]

        return res.lstrip("0")


if __name__ == "__main__":
    S = Solution()
    inputs = [
        ("1432219", 3),
        ("10200", 1),
        ("10", 2),
        ("139651", 3),
        ("654789", 3),
        ("1", 1),
        ("54321", 4),
        ("12345", 4),
        ("54321", 3),
        ("12345", 3),
    ]

    assert S.removeKdigits(*inputs[0]) == "1219"
    assert S.removeKdigits(*inputs[1]) == "200"
    assert S.removeKdigits(*inputs[2]) == "0"
    assert S.removeKdigits(*inputs[3]) == "131"
    assert S.removeKdigits(*inputs[4]) == "489"
    assert S.removeKdigits(*inputs[5]) == "0"
    assert S.removeKdigits(*inputs[6]) == "1"
    assert S.removeKdigits(*inputs[7]) == "1"
