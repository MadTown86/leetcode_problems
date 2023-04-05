import string

caps = string.ascii_uppercase
class Solution:
    def convertToTitle(self, num: int) -> str:
        if not num:
            return ''
        q, r = divmod(num - 1, 26)
        return self.convertToTitle(q) + caps[r]
