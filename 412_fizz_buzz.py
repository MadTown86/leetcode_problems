# https://leetcode.com/problems/fizz-buzz/

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for x in range(1, n + 1):
            if x % 3 == 0 and x % 5 == 0:
                res.append("FizzBuzz")
            elif x % 3 == 0 and x % 5 != 0:
                res.append("Fizz")
            elif x % 3 != 0 and x % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(x))
        return res


if __name__ == "__main__":
    S = Solution()
    inp = [3, 5, 15]

    assert S.fizzBuzz(inp[0]) == ["1", "2", "Fizz"]
    assert S.fizzBuzz(inp[1]) == ["1", "2", "Fizz", "4", "Buzz"]
    assert S.fizzBuzz(inp[2]) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]
