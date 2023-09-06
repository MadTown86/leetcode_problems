import re
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 0
        substrings = []
        a, b, n = 0, 1, len(s)
        while a < n - 1:
            substring = s[a:b]

        return longest



if __name__ == "__main__":
    S = Solution()
    inp = ['abcabcbb', 'bbbbb', 'pwwkew', 'cdd', 'au', 'aab']

    # assert S.lengthOfLongestSubstring(inp[0]) == 3
    # assert S.lengthOfLongestSubstring(inp[1]) == 1
    # assert S.lengthOfLongestSubstring(inp[2]) == 3
    assert S.lengthOfLongestSubstring(inp[3]) == 2
    # assert S.lengthOfLongestSubstring(inp[4]) == 2
    assert S.lengthOfLongestSubstring(inp[5]) == 2