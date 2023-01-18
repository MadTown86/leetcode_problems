from time import perf_counter

class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = 0
        x = str(x)
        b = len(x)-1
        m = (len(x)-1)/2
        if len(x) == 2:
            if x[0] != x[1]:
                return False
            else:
                return True
        elif len(x) % 2 == 0:
            while x[a] == x[b] and b >= 0 and a < len(x)-1:
                a = a + 1
                b = b - 1
            if x[a] != x[b]:
                return False
            else:
                return True
        elif len(x) % 2 != 0:
            while x[a] == x[b] and b != m and a != m:
                a = a + 1
                b = b - 1
            if x[a] != x[b]:
                return False
            else:
                return True


    # Fastest:
    def isPalindrome2(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        return False

    # Most Common
    def isPalindrome3(self, x: int) -> bool:
        y = str(x)
        if y == y[::-1]:
            return True
        else:
            return False

if __name__ == "__main__":
    S = Solution()
    start = perf_counter()
    res = S.isPalindrome2(12321232123212321232123212321232123212321232123212321232123212321232123212321232123212321)
    stop = perf_counter()
    timer = stop - start
    print(res)
    print(f'{timer:.8f}')