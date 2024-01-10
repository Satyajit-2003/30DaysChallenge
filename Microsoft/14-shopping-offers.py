from typing import List

# Use unbounded knapsack with memoization

class Solution:
    def helper(self, price: List[int], special: List[List[int]], needs: List[int]):
        need_t = tuple(needs)
        if need_t in self.hash:
            return self.hash[need_t]
        min_price = sum([price[i]*needs[i] for i in range(len(price))])
        for offer in special:
            if all(offer[i] <= needs[i] for i in range(len(price))):
                new_needs = [needs[i] - offer[i] for i in range(len(price))]
                min_price = min(
                    min_price,
                    offer[-1] + self.helper(price, special, new_needs)
                )
        self.hash[need_t] = min_price
        return min_price

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.hash = {}
        return self.helper(price, special, needs)
