import re

def main(s: str)-> bool:
        x = 1
        while x < len(s):
            sub = s[:x]
            print(f'{sub=}')
            mult = 1
            trialstring = ""
            while len(trialstring) <= len(s):
                trialstring = sub * mult
                if trialstring == s:
                    return True
                else:
                    mult += 1
            x += 1
        return False

"""faster solution O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n//2 + 1):
        # This excludes uneven strings that can't be divided into equal parts, smart
            if n % i == 0:
                substring = s[:i]
                # Based on the 'even' division, you only need to check to see if the substring multiplied by cursor is equal to S also smart
                    # don't have to build entire string and then check
                if substring * (n // i) == s:
                    return True
        return False
"""


if __name__ == "__main__":
    inputs = ["abab", "aba", "abcabcabcabc"]
    for i in inputs:
        print(main(i))