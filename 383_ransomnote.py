# https://leetcode.com/problems/ransom-note/
from collections import Counter

class Solution:
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        visited = [0] * 256
        a, b = 0, 0
        while b < len(magazine):
            ord_mag = ord(magazine[b])
            visited[ord_mag] += ord_mag
            b += 1
        while a < len(ransomNote):
            ordval = ord(ransomNote[a])
            if visited[ordval] < ordval:
                return False
            else:
                visited[ordval] -= ordval
                a += 1

        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        This is the better answer most likely because Counter is optimized for both time and memory vs. other
        algorithm.
        """
        cont = {}
        a, b = 0, 0
        c = Counter(magazine)
        d = Counter(ransomNote)
        for char in d.keys():
            if char not in c.keys():
                return False
            if c[char] < d[char]:
                return False
        return True

if __name__ == "__main__":
    S = Solution()
    inp = [('a', 'a'), ('aa', 'ab'), ('aa', 'aab'), ('abcdefg', 'aabbccdefg'), ('aaaaafffffg', 'aaaafg')]

    for prob in inp:
        print(S.canConstruct(*prob))
