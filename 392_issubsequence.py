# https://leetcode.com/problems/is-subsequence/
import re
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pattern, st, lt, ls = 0, 0, len(t), len(s)
        if ls == 0:
            return True
        if ls > lt:
            return False
        while pattern < ls:
            if ls-1-pattern > lt-st:
                return False
            if st < lt:
                if pattern == ls - 1 and st >= pattern and t[st] == s[pattern]:
                    return True
                elif s[pattern] == t[st] and st >= pattern:
                    pattern += 1
                    st += 1
                else:
                    st += 1
            else:
                return False
        return False


if __name__ == "__main__":
    inp = [('abc', 'ahbgdc'), ('axc', 'ahbgdc'), ('a', 'd'), ('abcd', 'adddbaaaeeecfffffeeed'), ('', ''), ('abc', 'a')]
    S = Solution()
    S.isSubsequence(*inp[0])
    assert S.isSubsequence(*inp[0]) == True
    assert S.isSubsequence(*inp[1]) == False
    assert S.isSubsequence(*inp[2]) == False
    assert S.isSubsequence(*inp[3]) == True
    assert S.isSubsequence(*inp[4]) == True
    assert S.isSubsequence(*inp[5]) == False
