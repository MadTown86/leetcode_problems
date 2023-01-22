from time import perf_counter
class Solution:
    def is_valid(self, s: str) -> bool:
        o, c, i, stak = ['(', '{', '['], [')', '}', ']'], 0, []
        while i <= len(s)-1:
            if s[i] in o:
                stak.append(s[i])
                i += 1
                continue
            else:
                if not stak:
                    return False
                else:
                    if stak[-1] != o[c.index(s[i])]:
                        return False
                    else:
                        stak.pop()
                        i += 1
                        continue
        return True

    def is_valid2(self, s: str) -> bool:
        o, c, stak = ['(', '{', '['], [')', '}', ']'], []
        stak = []
        for i in range(len(s) - 1):
            if s[i] in o:
                stak.append(s[i])
                i += 1
                continue
            else:
                if not stak:
                    return False
                else:
                    if stak[-1] != o[c.index(s[i])]:
                        return False
                    else:
                        stak.pop()
                        i += 1
                        continue
        return True

    def is_valid3(self, s: str) -> bool:
        opp, stak = {"{": "}", "[": "]", "(": ")"}, []
        for c in s:
            if c == '{' or c == '[' or c == '(':
                stak.append(c)
                continue
            else:
                if not stak:
                    return False
                else:
                    if c != opp[stak[-1]]:
                        return False
                    else:
                        stak.pop()
                        continue
        return True

if __name__ == "__main__":
    S = Solution()
    t_inputs = ["()(())()[][]"*10000, "()[]{}"*20000, "(]"]

    def benchit(inp: str) -> str:
        start = perf_counter()
        S.is_valid(inp)
        stop = perf_counter()
        start2 = perf_counter()
        S.is_valid2(inp)
        stop2 = perf_counter()
        start3 = perf_counter()
        S.is_valid3(inp)
        stop3 = perf_counter()
        res = f'VAL1: {stop-start:.10f}, VAL2: {stop2-start2:.10f}, VAL3: {stop3-start3:.10f}'
        return res

    for inp in t_inputs:
        print(benchit(inp))

