"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""

"""
Attempting to practice the re module a bit here
"""
import re #so ronery
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        need = re.compile(needle)
        match = re.search(need, haystack)
        if match:
            return match.start()
        else:
            return -1

"""

from functools import lru_cache
import timer
@lru_cache
def strStr(haystack: str, needle: str, pos: int = 0) -> int:
    if len(haystack) < len(needle):
        return -1
    if haystack[0:len(needle)] == needle:
        return pos
    else:
        pos += 1
        return strStr(haystack=haystack[1:], needle=needle, pos=pos)

def strStr2(haystack: str, needle: str, pos: int = 0) -> int:
    if len(haystack) < len(needle):
        return -1
    if haystack[0:len(needle)] == needle:
        return pos
    else:
        pos += 1
        return strStr(haystack=haystack[1:], needle=needle, pos=pos)

def strStr3(haystack: str, needle: str, pos: int = 0) -> int:
    i = 0
    while True:
        if haystack[i:len(needle)] == needle:
            return True
        else:
            continue

    return False


# I want to see if there is any real memory improvement or speed improvement when using memoryview, bytes, hash to compare
# vs. normal strings
def strStr4(haystack: str, needle: str) -> int:
    i = 0
    while i < len(needle):

        if hash(m[i:nl].tobytes()) == hash(n):
            return True
        else:
            i += 1
            continue

    return False



if __name__ == "__main__":
    test1 = "iamnotada;sldkfja;sldkfja;sldkfja;sldkfja;sldkfja;woeijra;wlifna;slkdfj;alskdfja;lskdfj;woeifja;efioja;soiefja;soiefja;soefija;sliefja;lsiefj;asliefja;soiefj;asilefja;sliefja;sliefja;sliefja;sliefja;sliefja;sliefj;asliefj;asleifja;sleifja;soeijf;wlkjenf;lwjnerflkewajrntg;alkerjta;lskdjf;aslkdfj;aoweijf;aoeing;aoinse;foiasjef;lakesnmf;lawknwjef;aosid" + "jf;asoing;aowienf;asdkljfbugglycornstuglybuggly"
    test2 = "ibuggly"
    print(strStr4(test2, "buggly"))

"""

import re

if __name__ == "__main__":
    st = "bugglysmelly"
    pattern = re.compile('ly')
    match = re.search(pattern, st)
    print(match.start())
