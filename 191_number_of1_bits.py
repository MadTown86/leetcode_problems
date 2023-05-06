class Solution:
    def hammingWeight(self, n: int) -> int:
        n = format(n, '032b')
        return str(n).count('1')


if __name__ == "__main__":
    S = Solution()
    n = 0b00000000000000000000000000001011
    m = 0b00000000000000000000000010000000
    l = 0b11111111111111111111111111111101
    assert S.hammingWeight(n) == 3
    assert S.hammingWeight(m) == 1
    assert S.hammingWeight(l) == 31