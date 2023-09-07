import re
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        substrings = []
        a, b, n = 0, 1, len(s)

        while a < n:
            subs = ''
            b = a
            while b < n:
                if s[b] not in subs:
                    subs += s[b]
                    b += 1
                else:
                    break
            if not substrings:
                substrings.append(subs)
            if max(list(map(lambda x: len(x), substrings))) <= len(subs):
                substrings.append(subs)
            a += 1

        return max(list(map(lambda j: len(j), substrings)))

    def lengthOfLongestSubstring2(self, s: str)->int:
        # https: // www.geeksforgeeks.org / length - of - the - longest - substring - without - repeating - characters /

        # If the length of the string is 0, return 0
        if len(s) == 0:
            return 0
        # If the length of the string is 1, return 1
        if len(s) == 1:
            return 1

        # Setting max length to the minimum value
        maxLength = 0

        # Set an array with all false values for all 256 characters in standard use
        # The main takeaway for me is the use of this to check if a character has already been in use
        # Using this array to set a true value and then always checking the ordinal value for True/False
        # Allows you to avoid having to re-trace.  It will continue to increment right and then reset itself
        # To false
        visited = [False] * 257

        # Set both pointers to 0
        left, right = 0, 0

        # The right will always increment to the end first, the left pointer will always increment only after right
        # has incremented to the last character and will always trail the right pointer
        while right < len(s):

            # This catches whether you have visited a value or not
            if visited[ord(s[right])]:

                # This while loop will continue to reset all values until it reaches a False value
                while visited[ord(s[right])]:

                    visited[ord(s[left])] = False
                    left += 1

            # This line sets the leading pointer (right) to True and then continues to increment forward
            visited[ord(s[right])] = True

            # This will check the max length at each increment forward while still finding a False
            maxLength = max(maxLength, right-left + 1)
            right += 1

        return maxLength


if __name__ == "__main__":
    S = Solution()
    inp = ['abcabcdb', 'bbbbb', 'pwwkew', 'cdd', 'au', 'aab']
    for x in inp:
        S.lengthOfLongestSubstring(x)

    assert S.lengthOfLongestSubstring2(inp[0]) == 4
    # assert S.lengthOfLongestSubstring(inp[1]) == 1
    # assert S.lengthOfLongestSubstring(inp[2]) == 3
    # assert S.lengthOfLongestSubstring(inp[3]) == 2
    # assert S.lengthOfLongestSubstring(inp[4]) == 2
    # assert S.lengthOfLongestSubstring(inp[5]) == 2
