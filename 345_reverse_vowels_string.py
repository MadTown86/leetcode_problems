# https://leetcode.com/problems/reverse-vowels-of-a-string/
from collections import deque
class Solution:
    def reverseVowels(self, s: str) -> str:
        l = [x for x in s]
        vbin = "aeiouAEIOU"
        x, y = 0, len(s)-1
        while x <= y:
            if l[x] in vbin:
                print('here')
                carry = l[x]
                if l[y] in vbin:
                    l[x] = s[y]
                    l[y] = carry
                    x += 1
                    y -= 1
                else:
                    y -= 1
                    continue
            else:
                x += 1
                continue
        return ''.join(x for x in l)

if __name__ == "__main__":
    inputs = ['hello', 'goodbye', 'magnificent']
    S = Solution()
    for arg in inputs:
        print(S.reverseVowels(arg))