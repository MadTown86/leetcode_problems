# https://leetcode.com/problems/excel-sheet-column-title/

import string

caps = string.ascii_uppercase


class Solution:
    def convertToTitle(self, num: int) -> str:
        if not num:
            return ''
        q, r = divmod(num-1, 26)
        return self.convertToTitle(q) + caps[r]

if __name__ == '__main__':
    S = Solution()

    # assert S.convertToTitle(1) == 'A'
    # assert S.convertToTitle(25) == 'Y'
    # assert S.convertToTitle(27) == 'AA'
    # print(S.convertToTitle(701))
    # assert S.convertToTitle(702) == 'ZZ'


    print(S.convertToTitle(18279))


