class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pass
        av, bv = 0, 0
        a = ''.join(x for x in reversed(a))
        b = ''.join(x for x in reversed(b))
        if len(a) > 1:
            for x in range(0, len(a)):
                if int(a[x]) == 1:
                    av += 2**x
        elif int(a[0]) == 1:
            av = 1
        if len(b) > 1:
            for x in range(0, len(b)):
                if int(b[x]) == 1:
                    bv += 2**x
        elif int(b[0]) == 1:
            bv = 1
        c = str(bin(av+bv))
        return c[2:]

if __name__ == "__main__":
    S = Solution()
    args = [['11', '1'], ['1010', '1011']]
    for arg in args:
        print(S.addBinary(*arg))