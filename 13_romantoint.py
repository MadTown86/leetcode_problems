class Solution:
    """
    My core mistakes:
    1. strings are indexable, never needed to createa  list.  I did realize this when I was already done with the
    problem, but again.  I need to remember this when I start.
    2. Too many bool statements that I believe HAVE to be checked
    3. To many variables that need to be assigned at each iteration of the while loop.

    Ways to improve:
    For string parsing, use indexes because direct indexing a string / list is the fastest way rather than storing
    the last variable in memory to do the comparison.

    Anyway.  Enough for now.
    """
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
        l = sw_bd[step.pop()]
        res += l
        l_l = l
        while step:
            char = step.pop()
            cur = sw_bd[char]
            if cur > l_l:
                l_l = cur
            if cur < l and cur < l_l:
                res -= cur
            elif cur > l:
                res += cur
            elif cur == l and cur < l_l:
                res -= cur
            elif cur == l and cur > l_l:
                res += cur
            elif cur == l and cur == l_l:
                res += cur
            l = cur

        return res

    # If I had an inkling of series math, I need to look through this one at some point to get the 2* logic
    # Example of faster problem
    def romanToInt2(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        res += d[s[0]]
        for i in range(1, len(s)):
            if d[s[i]] > d[s[i - 1]]:
                res += d[s[i]] - 2 * d[s[i - 1]]
            else:
                res += d[s[i]]
        return res

    # Slices are faster potentially, I also knew there was a way to slim down my conditional statements.
    # This is my real problem so I need to really understand HOW this problem didn't need all of the garbage I thought
    # That it did.
    def romanToInt3(self, s: str) -> int:
        def romanToInt(self, s: str) -> int:
            values = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
            }

            res = 0

            sLen = len(s)

            i = sLen - 1

            while i >= 0:
                if i > 0 and values[s[i]] > values[s[i - 1]]:
                    res += values[s[i]] - values[s[i - 1]]
                    i -= 2
                else:
                    res += values[s[i]]
                    i -= 1

            return res


















    def romanToInt(self, s: str) -> int:
        # Trying to mimic after knowing it is possible to create with just two conditional statements
            pass


if __name__ == "__main__":
    import timeit
    s = "MCMXCIV"
    SO = Solution()
    T = SO.romanToInt(s)

