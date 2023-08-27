class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l, r, under = moves.count('L'), moves.count('R'), moves.count('_')
        return abs(l-r) + under

if __name__ == "__main__":
    inputs = ['L_RL__R', '_R__LL_', '_______']
    S = Solution()
    assert S.furthestDistanceFromOrigin(inputs[0]) == 3
    assert S.furthestDistanceFromOrigin(inputs[1]) == 5
    assert S.furthestDistanceFromOrigin(inputs[2]) == 7