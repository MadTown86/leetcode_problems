class Solution:
    def is_valid(self, s: str) -> bool:
        o = ['(', '{', '[']
        c = [')', '}', ']']

        i = 0
        stak = []
        while i < len(s):
            if s[i] in o:
                stak.append(s[i])


