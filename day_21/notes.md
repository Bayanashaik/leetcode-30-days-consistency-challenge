# Day 21 Notes

## Problem 81: Find Most Frequent Vowel and Consonant  
**Link:** [LeetCode](https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/)  

### Approach  
- Use a dictionary for vowels (`a, e, i, o, u`) and another for consonants.  
- Count frequencies.  
- Take the max vowel frequency and max consonant frequency.  
- Return their sum.  

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  

---

## Problem 82: Check Balanced String  
**Link:** [LeetCode](https://leetcode.com/problems/check-balanced-string/)  

### Approach  
- Convert string to list of digits.  
- Sum digits at even indices and odd indices separately.  
- Return `True` if they are equal.  

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  

---

## Problem 83: Minimum Number of Chairs in a Waiting Room  
**Link:** [LeetCode](https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/)  

### Approach  
- Track current people inside with `count`.  
- Increase on `E` (enter) and decrease on `L` (leave).  
- Keep track of max `count` → minimum chairs required.  

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  

---

## Problem 84: Count the Number of Special Characters I  
**Link:** [LeetCode](https://leetcode.com/problems/count-the-number-of-special-characters-i/)  

### Approach  
- Separate lowercase and uppercase characters.  
- Convert uppercase to lowercase for comparison.  
- Count lowercase letters that also appear in uppercase.  

**Time Complexity:** O(n)  
**Space Complexity:** O(n)  

---
