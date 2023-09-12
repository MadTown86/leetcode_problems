# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution:
    def toHex(self, num: int) -> str:
        d = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        res = ""
        if num == 0:
            return "0"
        if num < 0:
            num = (1 << 32) + num
        while num > 0:
            if num % 16 < 10:
                res += str(num % 16)
            else:
                res += str(d[num % 16])
            num = num//16
        return res[::-1]


if __name__ == "__main__":
    S = Solution()
    inp = [26, -1]

    print(S.toHex(inp[0]))
    print(S.toHex(inp[1]))

    # assert S.toHex(inp[0]) == '1a'
    # assert S.toHex(inp[1]) == 'ffffffff'
