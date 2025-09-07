# Day 20 Notes

## Problem 77: Find N Unique Integers Sum up to Zero  
**Link:** [LeetCode - Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)  

### Approach  
- We need `n` unique integers whose sum is `0`.  
- Start by pairing numbers like `1` and `-1`, `2` and `-2`, etc.  
- If `n` is odd, add an extra `0`.  

### Complexity  
- **Time:** O(n)  
- **Space:** O(n)  

---

## Problem 78: Count Equal and Divisible Pairs in an Array  
**Link:** [LeetCode - Count Equal and Divisible Pairs in an Array](https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/)  

### Approach  
- Check all pairs `(i, j)` with `i < j`.  
- If `nums[i] == nums[j]` and `i * j` is divisible by `k`, count it.  

### Complexity  
- **Time:** O(n²)  
- **Space:** O(1)  

---

## Problem 79: Valid Palindrome  
**Link:** [LeetCode - Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)  

### Approach  
- Keep only alphanumeric characters and convert them to lowercase.  
- Compare the string with its reverse.  
- If they are equal, it’s a palindrome.  

### Complexity  
- **Time:** O(n)  
- **Space:** O(n)  

---

## Problem 80: Reverse Only Letters  
**Link:** [LeetCode - Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/)  

### Approach  
- Use two pointers (`i`, `j`).  
- Skip non-letter characters.  
- Swap letters from both ends.  
- Join back into a string.  

### Complexity  
- **Time:** O(n)  
- **Space:** O(n) (since strings are immutable)  

---
