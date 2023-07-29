from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        bins = []
        res = []
        for x in words:
            part = x.split(separator)
            print(part)
            res += part

        res2 = [x for x in res if len(x) > 0]
        return res2

if __name__ == "__main__":
    S = Solution()
    inputs = (["one.two.three","four.five","six"], '.')
    ['one', 'two', 'three', 'four', 'five', 'six']
    inputs2 = (['$easy$','$problem$'], '$')

    print(S.splitWordsBySeparator(inputs[0], inputs[1]))