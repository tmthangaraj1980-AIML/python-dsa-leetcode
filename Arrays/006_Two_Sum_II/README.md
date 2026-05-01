# 006 - Two Sum II (Input Array is Sorted)

## 🧩 Problem Statement
Given a **sorted array** of integers `numbers`, find two numbers such that they add up to a specific target number.

- Return indices (1-based index)
- Exactly one solution exists

---

## 💡 Approach (Two Pointer - Optimal)

- Since array is **sorted**, use two pointers:
  - `left` → start
  - `right` → end
- Calculate sum:
  - If sum == target → return answer
  - If sum < target → move left pointer
  - If sum > target → move right pointer

---

## 🧠 DSA Concepts Used
- Two Pointer Technique
- Array traversal
- Sorted array optimization

---

## 🔍 Dry Run


numbers = [2,7,11,15], target = 9

left = 0 (2)
right = 3 (15)

2 + 15 = 17 → too big → move right

2 + 11 = 13 → too big → move right

2 + 7 = 9 ✅
Return [1,2]


---

## 🚀 Code

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
⏱️ Time Complexity
O(n)
🧠 Space Complexity
O(1)
📸 Output

📌 Key Takeaways
Sorted array → use two pointers
Avoid hashmap when sorting helps
Very important interview pattern
🔗 LeetCode Link

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

👨‍💻 Author

Thangaraj
AIML Engineer | Python Developer