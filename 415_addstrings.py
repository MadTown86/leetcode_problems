# https://leetcode.com/problems/add-strings/

from collections import deque
from itertools import zip_longest
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        d = deque()
        hexmap = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        if len(num1) > len(num2):
            num2 = (len(num1) - len(num2))*'0' + num2
        elif len(num1) < len(num2):
            num1 = (len(num2) - len(num1))*'0' + num1
        carry = 0
        for x in range(len(num1)-1, -1, -1):
            if carry:
                calc = int(num1[x]) + int(num2[x]) + 1
                carry = 0
            else:
                calc = int(num1[x]) + int(num2[x])
            if calc >= 10 and x != 0:
                carry = 1
                calc = calc - 10
            d.appendleft(calc)
        return ''.join(str(x) for x in d)



if __name__ == "__main__":
    S = Solution()
    inp = [('11', '123'), ('456', '77'), ('0', '0'), ('123456789', '987654321')]

    print(S.addStrings(*inp[3]))
