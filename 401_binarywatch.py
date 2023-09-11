# https://leetcode.com/problems/binary-watch/description/
from typing import List
class Solution:
    """
    I had a solution that used distinct_permutations that I believe would be faster as I believe it wouldn't
    calculate all non-distinct permutations thereby being faster than this but Leetcode wouldn't import more_itertools
    """
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        output = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    output.append(f"{h}:{m:02}")
        return output

if __name__ == "__main__":
    S = Solution()
    inp = [1, 9]

    assert S.readBinaryWatch(inp[0]) == ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
    assert S.readBinaryWatch(inp[1]) == []