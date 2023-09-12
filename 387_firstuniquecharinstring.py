# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        min_pos = len(s)
        d = defaultdict(list)
        count = defaultdict(int)
        for ind in range(len(s)):
            d[s[ind]] += [ind]
            count[s[ind]] += 1


        for char, quant in sorted(count.items(), key=lambda char: count[char]):
            if quant == 1:
                if d[char][0] < min_pos:
                    min_pos = d[char][0]

        return -1 if min_pos == len(s) else min_pos

if __name__ == "__main__":
    S = Solution()
    inp = ['abba', 'babba', 'dabba', 'elephant', 'orange', 'eellk']

    assert S.firstUniqChar(inp[0]) == -1
    assert S.firstUniqChar(inp[1]) == -1
    assert S.firstUniqChar(inp[2]) == 0
    assert S.firstUniqChar(inp[3]) == 1
    assert S.firstUniqChar(inp[4]) == 0
    assert S.firstUniqChar(inp[5]) == 4