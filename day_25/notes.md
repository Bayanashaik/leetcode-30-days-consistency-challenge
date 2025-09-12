# Day 25 Notes

## Problem 97: Vowels Game in a String  
**Link:** [LeetCode](https://leetcode.com/problems/vowels-game-in-a-string/)  

### Approach  
- Check if the string contains any vowel (`a, e, i, o, u`).  
- If yes → Alice wins (`True`).  
- If no vowel → return `False`.  

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  

---

## Problem 98: Find the Index of the First Occurrence in a String  
**Link:** [LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)  

### Approach  
- Loop through all possible starting positions in `haystack`.  
- Compare substring of length `needle`.  
- Return index if found, else `-1`.  

**Time Complexity:** O((n-m+1) * m) in worst case  
**Space Complexity:** O(1)  

---

## Problem 99: Search Insert Position  
**Link:** [LeetCode](https://leetcode.com/problems/search-insert-position/)  

### Approach  
- Iterate through array.  
- If `nums[i] >= target`, return `i`.  
- If not found, return `len(nums)` (insert at end).  

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  

---

## Problem 100: Sqrt(x)  
**Link:** [LeetCode](https://leetcode.com/problems/sqrtx/)  

### Approach  
- Use Python `math.sqrt()` to compute square root.  
- Use `math.floor()` to return integer part.  

**Time Complexity:** O(1)  
**Space Complexity:** O(1)  

---
