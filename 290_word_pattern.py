# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        key_list = {}
        if len(pattern) != len(s.split(" ")):
            return False
        for x, y in zip(pattern, s.split(" ")):
            if x not in key_list.keys() and y not in key_list.values():
                key_list[x] = y
            if x not in key_list.keys() and y in key_list.values():
                return False
            if x in key_list.keys():
                if y != key_list[x]:
                    return False
                else:
                    continue

        return True


if __name__ == "__main__":
    inp = [("abba", "dog fish fish dog"), ("abba", "dog fish fish cat"), ("abba", "dog dog dog dog"), ("aaa", "aa aa aa aa")]
    S = Solution()
    for arg in inp:
        print(S.wordPattern(*arg))