# Day 24 Notes

## Problem 93: Detect Capital  
**Link:** [LeetCode](https://leetcode.com/problems/detect-capital/)  

### Approach  
- Valid cases:  
  1. All uppercase (e.g., "USA")  
  2. All lowercase (e.g., "leetcode")  
  3. Only first letter uppercase (e.g., "Google")  
- Return `True` if any of these are satisfied.  

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  

---

## Problem 94: To Lower Case  
**Link:** [LeetCode](https://leetcode.com/problems/to-lower-case/)  

### Approach  
- Iterate over each character.  
- Convert uppercase letters to lowercase manually using `.lower()`.  
- Append other characters as is.  

**Time Complexity:** O(n)  
**Space Complexity:** O(n)  

---

## Problem 95: Lexicographical Numbers  
**Link:** [LeetCode](https://leetcode.com/problems/lexicographical-numbers/)  

### Approach  
- Generate all numbers from `1` to `n`.  
- Convert to strings and sort lexicographically.  
- Convert back to integers.  

**Time Complexity:** O(n log n) (due to sorting)  
**Space Complexity:** O(n)  

---

## Problem 96: Find the Difference of Two Arrays  
**Link:** [LeetCode](https://leetcode.com/problems/find-the-difference-of-two-arrays/)  

### Approach  
- Collect numbers in `nums1` not in `nums2`.  
- Collect numbers in `nums2` not in `nums1`.  
- Convert both lists to sets to remove duplicates.  
- Return them as a list of lists.  

**Time Complexity:** O(n*m) (nested membership checks; can be optimized with sets)  
**Space Complexity:** O(n+m)  

---
