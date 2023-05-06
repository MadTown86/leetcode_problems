class Solution:
    def isHappy(self, n: int) -> bool:
        old_val_bin = []
        while n != 1:
            n = sum([int(x)**2 for x in str(n)])
            if n in old_val_bin:
                return False
            old_val_bin.append(n)
        return True

if __name__ == "__main__":
    S = Solution()
    assert S.isHappy(19) is True
    assert S.isHappy(2) is False
