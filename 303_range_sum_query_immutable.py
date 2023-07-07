from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        __slots__ = 'nums'
        self.data = nums
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.data[left:right+1]) if right < len(self.data) else sum(self.data[left:])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

if __name__ == "__main__":
    def createandexecute(nums: List[int], *args):
        NP = NumArray(nums)
        for a, b in args:
            print(NP.sumRange(a, b))

    input1 = [-2, -1, 0, 1, 2], [0, 2], [0, 3], [0, 4]
    input2 = [1, 1, 1, 1, 1, 1], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]

    print(createandexecute(*input1))