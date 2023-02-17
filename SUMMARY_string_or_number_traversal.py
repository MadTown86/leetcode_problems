from typing import List
def isPalindrome(self, x: int) -> bool:
    #https://leetcode.com/problems/palindrome-number/
    if x < 0:
        return False

    return str(x) == str(x)[::-1]

class Solution:
    def romanToInt(self, s: str) -> int:
        #https://leetcode.com/problems/roman-to-integer/
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #https://leetcode.com/problems/longest-common-prefix/
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix


#https://leetcode.com/problems/valid-parentheses/
    class Solution(object):
        def isValid(self, s):
            """
            :type s: str
            :rtype: bool
            """
            d = {'(': ')', '{': '}', '[': ']'}
            stack = []
            for i in s:
                if i in d:  # 1
                    stack.append(i)
                elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                    return False
            return len(stack) == 0  # 3

#https://leetcode.com/problems/length-of-last-word/
class Solution4(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordlist = s.split()
        if wordlist:
            return len(wordlist[-1])
        return 0

#https://leetcode.com/problems/plus-one/
class Solution5:
    def plusOne(self, digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]

#https://leetcode.com/problems/add-binary/
class Solution3:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sum = carry;
            if i >= 0 : sum += ord(a[i]) - ord('0') # ord is use to get value of ASCII character
            if j >= 0 : sum += ord(b[j]) - ord('0')
            i, j = i - 1, j - 1
            carry = 1 if sum > 1 else 0;
            res += str(sum % 2)

        if carry != 0 : res += str(carry);
        return res[::-1]

#https://leetcode.com/problems/climbing-stairs/
class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climb(n):
         if n==1: # only one step option is availble
             return 1
         if n ==2: # two options are possible : to take two 1-stpes or to only take one 2-steps
             return 2
         return climb(n-1) + climb(n-2)
        return climb(n)



