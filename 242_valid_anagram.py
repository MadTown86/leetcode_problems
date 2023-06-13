# https://leetcode.com/problems/valid-anagram/submissions/

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dds = defaultdict(int)
        ddt = defaultdict(int)

        for char in s:
            dds[char] += 1

        for char in t:
            ddt[char] += 1


        return dds == ddt

if __name__ == '__main__':
    S = Solution()
    s = 'anagram'
    t = 'nagaram'

    a = 'bat'
    b = 'cat'

    print(S.isAnagram(s, t))
    print(S.isAnagram(a, b))