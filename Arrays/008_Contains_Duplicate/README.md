# 008 - Contains Duplicate - 217

## 🧩 Problem Statement
Given an integer array `nums`, return `True` if any value appears at least twice in the array, and return `False` if every element is distinct.

---

## 💡 Approaches

### 🔹 1. Sorting Approach
- Sort the array
- Check adjacent elements
- If any two consecutive elements are same → duplicate exists

---

### 🔹 2. Set Approach (Optimal)
- Use a set to track seen elements
- While traversing:
  - If element already exists → duplicate found
  - Else → add to set

---

## 🧠 DSA Concepts Used
- Sorting
- Hashing (Set)
- Array traversal

---

## 🔍 Dry Run


nums = [1,2,3,1]

Step:
1 → add to set
2 → add
3 → add
1 → already exists → return True ✅


---

## 🚀 Code

### Sorting Approach
```python
# solution_sorting.py
class Solution:
    def containsDuplicate(self, nums):
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False
Set Approach (Optimized)
# solution_set.py
class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
⏱️ Complexity
Approach	Time	Space
Sorting	O(n log n)	O(1)
Set	O(n)	O(n)
📸 Output

📌 Key Takeaways
Sorting helps detect duplicates easily
Set provides faster lookup (O(1))
Hashing is preferred in interviews
🔗 LeetCode Link

https://leetcode.com/problems/contains-duplicate/

👨‍💻 Author

Thangaraj
AIML Engineer | Python Developer