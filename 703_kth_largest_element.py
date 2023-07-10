# https://leetcode.com/problems/kth-largest-element-in-a-stream/

from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pointer = k
        heapq.heapify(nums)
        self.data = nums

        round(11.1, )

    def add(self, val: int) -> int:
        heapq.heappush(self.data, val)
        return heapq.nlargest(self.pointer, self.data, key=None)[self.pointer]
        pass

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    inputs = [([3, [3, 5, 7, 7]], [3, 4, 4, 5])]
    def runtest(k: int, nums: List[int], *args):
        K = KthLargest(k, nums)
        for x in args:
            print(K.add(x))

    for x, y in inputs:
        print(x[0], x[1], y)
        runtest(x[0], x[1], y)
