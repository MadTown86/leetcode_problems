# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print(prices)
        if not prices or len(prices) == 1:
            return 0
        if len(prices) <= 2:
            return prices[1] - prices[0] if prices[1] - prices[0] > 0 else 0

        lowest = None
        highestval = 0
        for x in range(len(prices)):
            # print(f'PRICE: {prices[x]}')
            # print(f'lowest: {lowest}')
            # print(f'highestval: {highestval}')
            if lowest is None:
                lowest = prices[x]
                continue
            if lowest > prices[x]:
                lowest = prices[x]
                continue
            if lowest < prices[x] and highestval < prices[x] - lowest:
                highestval = prices[x] - lowest

        return highestval




if __name__ == "__main__":
    ppp = [2, 1] #0
    pp5 = [2, 4, 1]  # 2
    pp = [2, 1, 4, 6, 3, 1]  # 5  1 and 5
    pp2 = [7, 1, 5, 3, 6, 4]
    pp3 = [7, 6, 4, 3, 1]
    p4 = [100, 99, 98, 97, 81, 82, 40, 88, 36, 33, 0, 35]
    pp6 = [2, 1, 2, 1, 0, 1, 2]
    group = [pp, pp5, pp, pp2, pp3, p4]
    S = Solution()
    print(S.maxProfit(pp6))
