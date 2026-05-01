# 003 - Running Sum of 1D Array - 1480

## 🧩 Problem Statement
Given an array `nums`, return the running sum of the array.

---

## 💡 Approaches

### 🔹 1. Basic Approach
- Use new list
- Add previous sum manually

---

### 🔹 2. Built-in Approach
- Use Python functions like `accumulate` (itertools)

---

### 🔹 3. Optimized Approach (In-place)
- Modify the same array
- Add previous value to current value

---

## 🚀 Code

### Basic
```python
# solution_basic.py
def running_sum(nums):
    result = [nums[0]]

    for i in range(1, len(nums)):
        result.append(result[-1] + nums[i])

    return result

    Built-in
# solution_builtin.py
from itertools import accumulate

def running_sum(nums):
    return list(accumulate(nums))
Optimized
# solution_optimized.py
class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
⏱️ Complexity
Approach	Time	Space
Basic	O(n)	O(n)
Built-in	O(n)	O(n)
Optimized	O(n)	O(1)
📸 Output

🔗 LeetCode Link

https://leetcode.com/problems/running-sum-of-1d-array/

👨‍💻 Author

Thangaraj | AIML Engineer | Python Developer