# https://leetcode.com/problems/binary-watch/

from typing import List
from more_itertools import distinct_permutations


class Solution:
    def readBinaryWatch2(self, turnedOn: int) -> List[str]:
        """
        Can't use distinct itertools in leetcode
        """
        maxl = 10
        res = []
        l = [1] * turnedOn + [0] * (maxl - turnedOn)
        for item in distinct_permutations(l):
            hour = item[:4]
            hour_str = int("0" * 4 + "".join(str(x) for x in hour), 2)
            minute = item[4:]
            minute_str = int("0" * 2 + "".join(str(x) for x in minute), 2)
            if 0 <= hour_str <= 11 and 0 <= minute_str <= 59:
                res.append("{:01d}".format(hour_str) + ":" "{:02d}".format(minute_str))

        return res

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hour = "0000"
        hours = []
        for x in range(len(hour)):
            hour = "1" + hour[x + 1 :]
            hours.append(hour)

        print(hours)


if __name__ == "__main__":
    S = Solution()
    inp = [1, 9]

    S.readBinaryWatch(1)
    #
    # assert S.readBinaryWatch(inp[0]) == [
    #     "0:01",
    #     "0:02",
    #     "0:04",
    #     "0:08",
    #     "0:16",
    #     "0:32",
    #     "1:00",
    #     "2:00",
    #     "4:00",
    #     "8:00",
    # ]
    # assert S.readBinaryWatch(inp[1]) == []
