# 007 - Best Time to Buy and Sell Stock - 121

## 🧩 Problem Statement
You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.

Find the **maximum profit** you can achieve by:
- Buying on one day
- Selling on a later day

If no profit is possible, return `0`.

---

## 💡 Approach (Two Pointer - Optimal)

- Use two pointers:
  - `l` → buying day (lowest price so far)
  - `r` → selling day
- Traverse array:
  - If selling price is higher → calculate profit
  - Update maximum profit
  - If a lower price is found → update buying day

---

## 🧠 DSA Concepts Used
- Two Pointer Technique
- Greedy Approach
- Single pass optimization

---

## 🔍 Dry Run


prices = [7,1,5,3,6,4]

l = 0 (7), r = 1 (1) → lower price → move l

l = 1 (1), r = 2 (5) → profit = 4
l = 1 (1), r = 3 (3) → profit = 2
l = 1 (1), r = 4 (6) → profit = 5 ✅ max
l = 1 (1), r = 5 (4) → profit = 3

Final max profit = 5


---

## 🚀 Code

```python
class Solution:
    def maxProfit(self, prices):
        l = 0
        r = 1
        m = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                m = max(m, profit)
            else:
                l = r
            r += 1

        return m
⏱️ Time Complexity
O(n) → Single traversal
🧠 Space Complexity
O(1) → No extra space
📸 Output

📌 Key Takeaways
Track minimum price dynamically
Use two pointers for efficiency
Greedy approach ensures max profit
🔗 LeetCode Link

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

👨‍💻 Author

Thangaraj
AIML Engineer | Python Developer