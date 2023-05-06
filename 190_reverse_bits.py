class Solution:
    def reverseBits(self, n: int) -> int:
        x = int(''.join(x for x in reversed(format(n, '032b'))), base=2)
        return x

if __name__ == "__main__":
    n = int('0b00000010100101000001111010011100', base=2)
    m = int(0b11111111111111111111111111111101)
    S = Solution()
    S.reverseBits(n)
    S.reverseBits(m)
    assert S.reverseBits(n) == 964176192
    assert S.reverseBits(m) == 3221225471