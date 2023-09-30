# https://leetcode.com/contest/weekly-contest-363/problems/maximum-number-of-alloys/

from typing import List


class Solution:
    def maxNumberOfAlloys(
        self,
        n: int,
        k: int,
        budget: int,
        composition: List[List[int]],
        stock: List[int],
        cost: List[int],
    ) -> int:
        """
        n = quantity or index of metals
        k = quantity or index of machines

        budget = maximum alloys processed for accumulated cost of composition[k][n] while stock[n] >= 0
        stock = quantity of material initially on hand
        """
        res = []
        for i in range(k):
            alloycnt = 0
            spend = 0
            to_buy = []
            no_budget = False

            for j in range(n):
                if stock[j] < composition[i][j]:
                    to_buy.append(composition[i][j] - stock[j])
                else:
                    to_buy.append(0)
            print(to_buy)
            while sum(to_buy) > 0:
                for k in range(len(to_buy)):
                    purchase_cost = cost[k] * to_buy[k]
                    if spend + purchase_cost < budget:
                        spend += purchase_cost
                        stock[k] += to_buy[k]
                        to_buy[k] = 0
                    else:
                        no_budget = True
                        for x in range(len(to_buy)):
                            to_buy[x] = 0
            while spend < budget:
                for l in range(n):
                    purchase_cost = cost[l] * composition[i][l]
                    if spend + purchase_cost < budget:
                        spend += purchase_cost
                        stock[l] += composition[i][l]
                    else:
                        spend += purchase_cost

            print(stock)
            if no_budget:
                break
            else:
                quantity = 0
                for j in range(n):
                    qty_check = stock[j] / composition[i][j]
                    if qty_check > quantity:
                        quantity = qty_check
            res.append(quantity)
        return max(res)


if __name__ == "__main__":
    S = Solution()
    inp = [(3, 2, 15, [[1, 1, 1], [1, 1, 10]], [0, 0, 0], [1, 2, 3])]
    print(S.maxNumberOfAlloys(*inp[0]))
