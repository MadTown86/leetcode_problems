"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""
from functools import lru_cache
from timeit import timeit
timeit()
def strStr(haystack: str, needle: str, pos: int = 0) -> int:
    if len(haystack) < len(needle):
        return -1
    if haystack[0:len(needle)] == needle:
        return pos
    else:
        pos += 1
        return strStr(haystack=haystack[1:], needle=needle, pos=pos)

if __name__ == "__main__":
    test1 = "iamnotabugglycornstuglybuggly"

    print(strStr(test1, "buggly", 0))
