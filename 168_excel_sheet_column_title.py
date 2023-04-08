import string

caps = string.ascii_uppercase
class Solution:
    def convertToTitle(self, num: int) -> str:
        if not num:
            return ''
        q, r = divmod(num - 1, 26)
        return self.convertToTitle(q) + caps[r]

if __name__ == '__main__':
    nums = 1547
    S = Solution()
    print(S.convertToTitle(nums))


"""
First step - divide number by 26 recursively, add 
"""
