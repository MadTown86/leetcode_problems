# https://leetcode.com/problems/remove-k-digits/description/

import math


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = num[k:]
        a, b = 0, k
        print(num[a], num[k])
        while k:
            if num[a] > num[b]:
                k -= 1
                a += 1








if __name__ == "__main__":
    S = Solution()
    with open("C:\\REPOSITORIES\\PYTHON\\leetcode_problems\\402_input.txt", 'r') as inp:
        txt = inp.read()

    with open("C:\\REPOSITORIES\\PYTHON\\leetcode_problems\\402_answer.txt", 'r') as ansfile:
        ans = ansfile.read()

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
        ("10", 1),
        ("100", 1),
        ("112", 1),
        ("12345", 2),
        (txt, 1000)
    ]

    assert S.removeKdigits(*inputs[0]) == "1219"
    assert S.removeKdigits(*inputs[1]) == "200"
    assert S.removeKdigits(*inputs[2]) == "0"
    assert S.removeKdigits(*inputs[3]) == "131"
    assert S.removeKdigits(*inputs[4]) == "489"
    assert S.removeKdigits(*inputs[5]) == "0"
    assert S.removeKdigits(*inputs[6]) == "1"
    assert S.removeKdigits(*inputs[7]) == "1"
    assert S.removeKdigits(*inputs[8]) == "21"
    assert S.removeKdigits(*inputs[9]) == "12"
    assert S.removeKdigits(*inputs[10]) == "0"
    assert S.removeKdigits(*inputs[11]) == "0"
    assert S.removeKdigits(*inputs[12]) == "11"
    assert S.removeKdigits(*inputs[13]) == "123"
    # myres = S.removeKdigits(*inputs[14])
    # for mine, theirs in zip(myres, ans):
    #     print(f'{mine=} :: {theirs=}')
    # assert S.removeKdigits(*inputs[14]) == ans

