# https://leetcode.com/problems/valid-palindrome/
import string
punct = string.punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '')
        s = s.lower()
        for x in punct:
            s = s.replace(x, '')
        if not s:
            return True
        s2 = reversed(s)
        for x, y in zip(s, s2):
            if x != y:
                return False
        return True



if __name__ == '__main__':
    sss = 'crap,: sdfs'
    ex2 = "A man, a plan, a canal: Panama"
    S = Solution()
    print(S.isPalindrome(ex2))