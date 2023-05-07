class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a, d = 0, {}
        while a <= len(s) - 1:
            if s[a] not in d.keys() and t[a] not in d.values():
                d[s[a]] = t[a]
                a += 1
            elif s[a] in d.keys() and t[a] == d[s[a]]:
                a += 1
            elif s[a] not in d.keys() and t[a] in d.values():
                return False
            elif s[a] in d.keys() and t[a] != d[s[a]]:
                return False
        return True


if __name__ == "__main__":
    S = Solution()
    inp1 = ['egg', 'add']
    inp2 = ['foo', 'bar']
    inp3 = ['paper', 'title']
    assert S.isIsomorphic(*inp1) is True
    assert S.isIsomorphic(*inp2) is False
    assert S.isIsomorphic(*inp3) is True