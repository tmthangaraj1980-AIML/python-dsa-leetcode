# 005 - Longest Substring Without Repeating Characters  - 3

## 🧩 Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters.

---

## 💡 Approach (Optimized - Sliding Window)

- Use a **set** to store unique characters
- Maintain two pointers:
  - `left` → start of window
  - `right` → end of window
- Expand window using `right`
- If duplicate found:
  - Remove characters from left
  - Move `left` forward
- Update maximum length at each step

---

## 🧠 DSA Concepts Used
- Sliding Window
- Two Pointer Technique
- Hash Set for fast lookup (O(1))

---

## 🔍 Dry Run


s = "abcabcbb"

Step:
a → abc → length = 3
Next 'a' repeats → move left
Window becomes "bca"
Continue...

Final max length = 3


---

## 🚀 Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.discard(s[left])
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
⏱️ Time Complexity
O(n) → Each character visited at most twice
🧠 Space Complexity
O(n) → Set stores unique characters
📸 Output

📌 Key Takeaways
Sliding window avoids nested loops
Efficient for substring problems
Set helps maintain uniqueness
🔗 LeetCode Link

https://leetcode.com/problems/longest-substring-without-repeating-characters/

👨‍💻 Author

Thangaraj
AIML Engineer | Python Developer