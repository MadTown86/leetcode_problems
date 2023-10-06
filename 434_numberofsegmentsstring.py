# https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution:
    def countSegments(self, s: str) -> int:
        l = s.split(' ')
        res = []
        for x in range(len(l)):
            if l[x] == '':
                continue
            res.append(l[x])
        return len(res)

    def countSegments2(self, s: str) -> int:
        count = 0
        if len(s) > 1:
            for x in range(1, len(s)):
                if s[x-1] != ' ' and s[x] == ' ':
                    count += 1
                if x == len(s)-1 and s[x] != ' ':
                    count += 1
            return count
        else:
            if s[0] != ' ':
                return 1
            else:
                return 0

if __name__ == "__main__":
    S = Solution()
    inp = ['Hello, my name is John', 'Hello', '  c,  d, f, jj, l', 'a', ' ', 'a ', ' a']
    print(S.countSegments2(inp[6]))