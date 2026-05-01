# 002 - Valid Palindrome - 125

## 🧩 Problem Statement
Given a string `s`, return `True` if it is a palindrome, otherwise return `False`.

- Only alphanumeric characters are considered
- Ignore cases (A == a)

---

## 💡 Approach (Two Pointer - Optimal)

- Use two pointers:
  - `left` → start of string
  - `right` → end of string
- Move both pointers toward center
- Skip non-alphanumeric characters
- Compare characters (case insensitive)
- If mismatch → return False
- If all match → return True

---

## 🧠 DSA Concept Used

### ✅ Two Pointer Technique
- Used to compare elements from both ends
- Efficient for palindrome problems
- Avoids extra space usage

### ✅ String Handling
- `isalnum()` → checks alphanumeric
- `lower()` → case normalization

---

## 🔍 Dry Run

Input:s = "A man, a plan, a canal: Panama"


Steps:
- Ignore spaces, commas, colon
- Compare:
  - A == a ✔
  - m == m ✔
  - continue...

Final → All match → return True

---

## 🚀 Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True


        Time Complexity
O(n) → Single pass
🧠 Space Complexity
O(1) → No extra space
📸 Output

📌 Key Takeaways
Two pointer is powerful for string problems
Avoid extra memory when possible
Clean and optimal solution
🔗 LeetCode Link

https://leetcode.com/problems/valid-palindrome/

👨‍💻 Author

Thangaraj
AIML Engineer | Python Developer