# https://leetcode.com/contest/weekly-contest-361/problems/count-symmetric-integers/
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric = 0
        for x in range(low, high + 1):
            if len(str(x)) % 2 != 0:
                continue
            if len(str(x)) < 2:
                continue
            stringed = str(x)
            if len(stringed) == 2:
                if int(stringed[0]) == int(stringed[1]):
                    symmetric += 1
                    continue
            if len(stringed) > 2:
                first, second = (
                    stringed[len(stringed) // 2 :],
                    stringed[: len(stringed) // 2],
                )
                if sum(int(x) for x in first) == sum(int(x) for x in second):
                    symmetric += 1

        return symmetric


if __name__ == "__main__":
    input = [(1, 100), (1200, 1230), (1, 10000000)]

    S = Solution()
    assert S.countSymmetricIntegers(*input[0]) == 9
    assert S.countSymmetricIntegers(*input[1]) == 4

    print(S.countSymmetricIntegers(*input[2]))
