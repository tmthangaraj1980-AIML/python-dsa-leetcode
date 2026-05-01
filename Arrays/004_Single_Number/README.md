# 004 - Single Number - 136

## 🧩 Problem Statement
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

---

## 💡 Approaches

### 🔹 1. Basic Approach (Brute Force)
- Loop through each number
- Use `count()` to check frequency
- Return the number that appears only once

---

### 🔹 2. Built-in Approach (Math Trick)
- Use Python `set()` to get unique elements
- Apply formula:

single number = 2 × sum(set(nums)) − sum(nums)

---

## 🧠 DSA Concepts Used
- Frequency counting
- Set operations
- Mathematical manipulation

---

## 🔍 Dry Run


nums = [5,1,5,2,1]

set(nums) = {1,2,5}

2 * sum(set(nums)) = 2 * (1+2+5) = 16
sum(nums) = 5+1+5+2+1 = 14

Result = 16 - 14 = 2 ✅


---

## 🚀 Code

### Basic
```python
class Solution:
    def singleNumber(self, nums):
        for num in nums:
            if nums.count(num) == 1:
                return num
Built-in
def single_number(nums):
    return 2 * sum(set(nums)) - sum(nums)

nums = [5,1,5,2,1]
print(single_number(nums))
⏱️ Complexity
Approach	Time	Space
Basic	O(n²)	O(1)
Built-in	O(n)	O(n)
📸 Output

📌 Key Takeaways
Brute force is simple but slower
Built-in methods improve efficiency
Understanding patterns helps optimization
🔗 LeetCode Link

https://leetcode.com/problems/single-number/

👨‍💻 Author

Thangaraj
AIML Engineer | Python Developer