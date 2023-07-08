# https://leetcode.com/problems/reverse-string/

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        x, y = 0, len(s)-1
        while x <= y:
            carry = s[y]
            s[y] = s[x]
            s[x] = carry
            x += 1
            y -= 1
        print(s)

# for i in range(len(s)//2): s[i],s[-i-1] = s[-i-1],s[i]

if __name__ == "__main__":
    inputs = [[x for x in 'hello']]
    S = Solution()
    for arg in inputs:
        S.reverseString(arg)