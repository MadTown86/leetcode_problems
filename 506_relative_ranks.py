# https://leetcode.com/problems/relative-ranks/

from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medalists = {
            0: 'Gold Medal',
            1: 'Silver Medal',
            2: 'Bronze Medal'
        }
        temp = [x for x in sorted(score, reverse=True)]
        res = []
        for x in score:
            rank = temp.index(x)
            if rank in medalists.keys():
                res.append(medalists[rank])
            else:
                res.append(str(rank+1))
        return res


if __name__ == "__main__":
    inputs = [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
    S = Solution()
    for x in inputs:
        print(S.findRelativeRanks(x))

