# 009 - Maximum Subarray - 53

## 🧩 Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

---

## 💡 Approach (Kadane’s Algorithm - Optimal)

- Traverse the array once
- At each step:
  - Decide whether to start a new subarray
  - Or continue the existing subarray
- Keep track of:
  - Current sum (`c`)
  - Maximum sum (`m`)

---

## 🧠 DSA Concepts Used
- Dynamic Programming
- Greedy Approach
- Array Traversal

---

## 🔍 Dry Run


nums = [-2,1,-3,4,-1,2,1,-5,4]

Step:
c = -2, m = -2

i = 1 → c = max(1, -1) = 1 → m = 1
i = 2 → c = max(-3, -2) = -2 → m = 1
i = 3 → c = max(4, 2) = 4 → m = 4
i = 4 → c = max(-1, 3) = 3 → m = 4
i = 5 → c = max(2, 5) = 5 → m = 5
i = 6 → c = max(1, 6) = 6 → m = 6
i = 7 → c = max(-5, 1) = 1 → m = 6
i = 8 → c = max(4, 5) = 5 → m = 6

Final Answer = 6 ✅


---

## 🚀 Code

```python
class Solution:
    def maxSubArray(self, nums):
        m = nums[0]
        c = nums[0]

        for i in range(1, len(nums)):
            c = max(nums[i], c + nums[i])
            m = max(m, c)

        return m
⏱️ Time Complexity
O(n) → Single traversal
🧠 Space Complexity
O(1) → No extra space used
📸 Output

📌 Key Takeaways
Kadane’s Algorithm is used for maximum subarray problems
Ignore negative prefix sum
Always track global maximum
🔗 LeetCode Link

https://leetcode.com/problems/maximum-subarray/

👨‍💻 Author

Thangaraj
AIML Engineer | Python Developer