"""
BEST TIME TO BUY AND SELL STOCK
--------------------------------
Given an array `prices` where prices[i] is the stock price on day i,
return the maximum profit from one buy and one sell.
You must buy before you sell. Return 0 if no profit is possible.

Example:
Input : prices = [7, 1, 5, 3, 6, 4]
Output: 5   # Buy day 2 (price=1), sell day 5 (price=6)
"""


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE
# ─────────────────────────────────────────────
"""
Try every pair (buy day i, sell day j) where i < j.

Time  : O(n²)
Space : O(1)
"""

def max_profit_brute(prices):
    max_profit = 0
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit


# ─────────────────────────────────────────────
# APPROACH 2 — OPTIMAL (Sliding Window / Greedy)
# ─────────────────────────────────────────────
"""
Track the minimum price seen so far. At each day,
compute profit if sold today and update the max.

Trace (prices = [7, 1, 5, 3, 6, 4]):
  price=7 → min=7  profit=0
  price=1 → min=1  profit=0
  price=5 → min=1  profit=4
  price=3 → min=1  profit=4
  price=6 → min=1  profit=5  ← max
  price=4 → min=1  profit=5

Time  : O(n)
Space : O(1)
"""

def max_profit_optimal(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit


# ─────────────────────────────────────────────
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit_brute(prices))    # 5
    print(max_profit_optimal(prices))  # 5