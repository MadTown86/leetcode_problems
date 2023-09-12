# https://leetcode.com/problems/longest-palindrome/
from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = defaultdict(int)
        for char in sorted(s, key=lambda char: s.count(char)):
            c[char] += 1
        res = ''
        count = 0
        if len(c.keys()) == 1:
            return len(s)
        if len(c.keys()) == 2:
            for a in c.keys():
                if c[a] % 2 == 0:
                    return len(s)
        for char, cc in c.items():
            if count == 0 and cc == 1:
                res += char
                count += 1
                continue
            while cc >= 2:
                res =char + res + char
                cc -= 2
                count += 2
        return len(res)

if __name__ == "__main__":
    S = Solution()
    inp = ["abccccdd", 'a', 'abbacddeeef', 'ccc', 'ababababa', "zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez"]
    # assert S.longestPalindrome(inp[0]) == 7
    # assert S.longestPalindrome(inp[1]) == 1
    # assert S.longestPalindrome(inp[2]) == 9
    # assert S.longestPalindrome(inp[3]) == 3
    # assert S.longestPalindrome(inp[4]) == 9
    assert S.longestPalindrome(inp[5]) == 55

    print()



