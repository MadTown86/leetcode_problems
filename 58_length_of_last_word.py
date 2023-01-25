from time import perf_counter

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        y = -1
        if not s[y].isalpha():
            while True:
                if s[y].isalpha():
                    x = y
                    break
                else:
                    y -= 1
        else:
            y = 0
            x = -1
        while True:
            if s[x] == s[0]:
                break
            if s[x].isalpha():
                x -= 1
            else:
                break
        return abs(x-y)

if __name__ == "__main__":
    S = Solution()
    args = ["a ", "a" , "Hello", " fly me  to  the  moon  ", "a b c d elf 55"]

    def perfit(func, args):
        start = perf_counter()
        print(f'RESULT: {func(args)}')
        stop = perf_counter()
        print(f'TIME: {stop-start:.10f}')

    for arg in args:
        perfit(S.lengthOfLastWord, arg)
