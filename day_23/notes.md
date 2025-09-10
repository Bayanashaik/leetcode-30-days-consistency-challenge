# Day 23 Notes

## Problem 89: Convert Integer to the Sum of Two No-Zero Integers  
**Link:** [LeetCode](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)  

### Approach  
- Loop from 1 to n-1.  
- Check if both `i` and `n-i` contain no zero (`'0' not in str(x)`).  
- Return the first valid pair.  

**Time Complexity:** O(n * log(n)) (due to string conversion)  
**Space Complexity:** O(1)  

---

## Problem 90: Reverse Vowels of a String  
**Link:** [LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/)  

### Approach  
- Use two pointers: `i` from start, `j` from end.  
- Swap vowels when both are vowels.  
- Continue until `i >= j`.  

**Time Complexity:** O(n)  
**Space Complexity:** O(n) (for string conversion to list)  

---

## Problem 91: First Unique Character in a String  
**Link:** [LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)  

### Approach  
- Count frequency of each character.  
- Return the index of the first character with frequency 1.  
- If none found, return `-1`.  

**Time Complexity:** O(n)  
**Space Complexity:** O(1) (since only lowercase letters)  

---

## Problem 92: Number of Segments in a String  
**Link:** [LeetCode](https://leetcode.com/problems/number-of-segments-in-a-string/)  

### Approach  
- Use `split()` to break the string into words.  
- Count the number of non-empty parts.  

**Time Complexity:** O(n)  
**Space Complexity:** O(n) (for storing split words)  

---
