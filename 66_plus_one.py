from typing import List
from time import perf_counter

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits:
            if digits[-1] < 9:
                digits[-1] += 1
                return digits
            else:
                if digits[-1] == 9:
                    for x in range(-1, -(len(digits)+1), -1):
                        if x == -len(digits) and digits[0] == 9:
                            digits[0] = 1
                            digits.append(0)
                            return digits
                        elif x == -len(digits):
                            digits[0] += 1
                            return digits
                        elif digits[x] == 9:
                            digits[x] = 0
                        else:
                            digits[x] += 1
                            return digits

                else:
                    digits[-1] += 1
                    return digits
        else:
            return [1]

if __name__ == "__main__":
    S = Solution()
    args = [[1, 2, 3], [4, 3, 2, 1], [9, 9, 9, 9], [0], [9], [], [8, 9, 9, 9]]

    for arg in args:
        argc = arg[:]
        start = perf_counter()
        res = S.plusOne(arg)
        print(f'ARG: {argc} || RES: {res}')
        stop = perf_counter()
        print(f'TIME: {stop-start:.10f}')
