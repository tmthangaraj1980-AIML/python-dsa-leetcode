# 001 - Two Sum

## 🧩 Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

- Each input has exactly one solution
- You cannot use the same element twice
- You can return the answer in any order

---

## 💡 Approach (Optimized - HashMap)

Instead of checking all pairs (Brute Force), we use a **HashMap (Dictionary)** to reduce time complexity.

### 🔹 Idea:
- While traversing the array, store each number in a dictionary
- For every number, calculate:
  
  n = target - current number

- Check:
  - If complement already exists in dictionary → solution found
  - Else → store current number

---

## 🧠 DSA Concept Used

### ✅ Hashing (Dictionary in Python)

- Provides **O(1)** lookup time
- Helps avoid nested loops
- Stores values with their indices

---

## 🔍 Dry Run

Input:
nums = [2, 7, 11, 15], target = 9

Steps:

- i = 0 → num = 2  
  n = 7 → not found → store {2:0}

- i = 1 → num = 7  
  n = 2 → found in dictionary ✅  

Return → [0, 1]

---

## 🚀 Code (Optimized)

```python
class Solution:
    def twoSum(self, nums, target):
        s = {}

        for i, num in enumerate(nums):
            n = target - num

            if n in seen:
                return [s[n], i]

            s[num] = i



 Time Complexity
O(n) → Single traversal
🧠 Space Complexity
O(n) → Dictionary storage
📸 Output

📌 Key Takeaways
Avoid brute force when possible
Use hashing for fast lookup
Reduces complexity from O(n²) → O(n)
🔗 LeetCode Link

https://leetcode.com/problems/two-sum/

👨‍💻 Author

Thangaraj
AIML Engineer | Python Developer