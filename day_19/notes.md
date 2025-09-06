# Day 19 Notes

## Problem 73: Valid Anagram  
**Link:** [LeetCode - Valid Anagram](https://leetcode.com/problems/valid-anagram/)  

### Approach  
- First, check if both strings `s` and `t` have the same length. If not, return `False`.  
- Create a dictionary `d` for counting characters in `s`.  
- Create another dictionary `e` for counting characters in `t`.  
- Compare both dictionaries. If any mismatch is found, return `False`.  
- Otherwise, return `True`.  

### Complexity  
- **Time:** O(n)  
- **Space:** O(n)  

---

## Problem 74: Reverse String  
**Link:** [LeetCode - Reverse String](https://leetcode.com/problems/reverse-string/)  

### Approach  
- Use a two-pointer technique: swap the first element with the last, the second with the second-last, and so on.  
- Iterate till the middle of the array (`len(s)//2`).  
- Since modifications are in-place, return `s`.  

### Complexity  
- **Time:** O(n)  
- **Space:** O(1)  

---

## Problem 75: Find the Difference  
**Link:** [LeetCode - Find the Difference](https://leetcode.com/problems/find-the-difference/)  

### Approach  
- Count characters of `s` and store them in dictionary `d`.  
- Count characters of `t` and store them in dictionary `e`.  
- The extra character in `t` will either not exist in `s` or its frequency will be greater than in `s`.  
- Return that extra character.  

### Complexity  
- **Time:** O(n)  
- **Space:** O(n)  

---

## Problem 76: Longest Palindrome  
**Link:** [LeetCode - Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)  

### Approach  
- Count frequency of each character.  
- If frequency is even, add it fully to the result.  
- If frequency is odd, add `freq - 1` to the result and keep track that at least one odd exists.  
- At the end, if there was an odd frequency, add `1` (for the middle character).  

### Complexity  
- **Time:** O(n)  
- **Space:** O(n)  

---
