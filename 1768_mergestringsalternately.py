# https://leetcode.com/problems/merge-strings-alternately/
class Solution:
    def mergeAlternately2(self, word1: str, word2: str) -> str:
        """
        Scored higher, most likely because zip reduces the amount of necessary iterations
        """
        res = ''
        for x, y in zip(word1, word2):
            if x:
                res += x
            if y:
                res += y
        if len(word2) > len(word1):
            res += word2[len(word1):]
        else:
            res += word1[len(word2):]
        return res

    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        counter = 0
        for x in word1:
            res += x
            if len(word2) > counter:
                res += word2[counter]
                counter += 1

        if len(word1) < len(word2):
            res += word2[len(word1):]

        return res


if __name__ == "__main__":
    S = Solution()

    inp = [('abc', 'pxyz'), ('abcd', 'xy'), ('abc', '')]
    assert S.mergeAlternately(*inp[0]) == 'apbxcyz'
    assert S.mergeAlternately(*inp[1]) == 'axbycd'
    assert S.mergeAlternately(*inp[2]) == 'abc'