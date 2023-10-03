# https://leetcode.com/problems/add-strings/

from collections import deque
from itertools import zip_longest
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        d = deque()
        hexmapp = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for x, y in zip_longest(''.join(x for x in reversed(num1)), ''.join(x for x in reversed(num2)), fillvalue='0'):
            carry = 0
            summ = hexmapp[x] + hexmapp[y] + carry
            if summ > 9:
                carry = 1
                d.appendleft(str(summ))
            else:
                d.appendleft(str(summ))
                carry = 0
        return ''.join(x for x in d)

if __name__ == "__main__":
    S = Solution()
    inp = [('11', '123'), ('456', '77'), ('0', '0')]

    print(S.addStrings(*inp[0]))
    print(S.addStrings(*inp[1]))
