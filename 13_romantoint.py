class Solution:
    def romanToInt(self, s: str) -> int:
        sw_bd = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1

        }

        res = 0
        if len(s) == 1:
            res += sw_bd[s]
            return res

        step = list(s)
        last = sw_bd[step.pop()]
        res += last
        last_largest = last
        while step:
            char = step.pop()
            cur = sw_bd[char]
            if cur > last_largest:
                last_largest = cur
            if cur < last and cur < last_largest:
                res -= cur
            elif cur > last:
                res += cur
            elif cur == last and cur < last_largest:
                res -= cur
            elif cur == last and cur > last_largest:
                res += cur
            elif cur == last and cur == last_largest:
                res += cur
            last = cur

        return res

if __name__ == "__main__":
    import timeit
    s = "MCMXCIV"
    SO = Solution()
    T = SO.romanToInt(s)

