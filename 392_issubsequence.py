# https://leetcode.com/problems/is-subsequence/
import re
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pattern, st = 0, 0

        while pattern < len(s):
            if s[pattern] in t:


if __name__ == "__main__":
    inp = [('abc', 'ahbgdc'), ('axc', 'ahbgdc')]
    S = Solution()
    S.isSubsequence(*inp[0])
    # assert S.isSubsequence(*inp[0]) == True
    # assert S.isSubsequence(*inp[1]) == False
