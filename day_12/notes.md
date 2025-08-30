# 📘 Day 12 – LeetCode Problems Notes  

---

## 🔹 Problem 45: Maximum Difference Between Increasing Elements  
**Link:** [LeetCode 2016](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)  

### 📝 Problem Statement  
Given an array `nums`, return the maximum difference `nums[j] - nums[i]` such that `j > i` and `nums[j] > nums[i]`.  
If no such pair exists, return `-1`.  

### 💡 Approach  
- Initialize `min_v` as the first element.  
- Traverse from index `1` to end.  
- If `nums[j] > min_v`, calculate difference and update maximum.  
- Always keep track of the minimum value seen so far.  

### ⏱️ Complexity  
- **Time:** O(n) (one pass)  
- **Space:** O(1)  

---

## 🔹 Problem 46: Two Furthest Houses With Different Colors  
**Link:** [LeetCode 2078](https://leetcode.com/problems/two-furthest-houses-with-different-colors/)  

### 📝 Problem Statement  
You are given an array `colors` where each element represents the color of a house.  
Find the maximum distance between **two houses with different colors**.  

### 💡 Approach  
- Check from the rightmost house back to the first → first mismatch with `colors[0]` gives a distance.  
- Check from the leftmost house up to the last → first mismatch with `colors[n-1]` gives another distance.  
- Take maximum of the two.  

### ⏱️ Complexity  
- **Time:** O(n)  
- **Space:** O(1)  

---

## 🔹 Problem 47: Ugly Number  
**Link:** [LeetCode 263](https://leetcode.com/problems/ugly-number/)  

### 📝 Problem Statement  
An ugly number is a number whose prime factors are only **2, 3, or 5**.  
Return `True` if `n` is an ugly number, otherwise `False`.  

### 💡 Approach  
- If `n <= 0`, return `False`.  
- Repeatedly divide `n` by `2`, `3`, and `5` while possible.  
- If we end up with `1`, it is ugly; else not.  

### ⏱️ Complexity  
- **Time:** O(log n) (division process)  
- **Space:** O(1)  

---

## 🔹 Problem 48: Count Negative Numbers in a Sorted Matrix  
**Link:** [LeetCode 1351](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)  

### 📝 Problem Statement  
Given an m x n matrix `grid` sorted in **non-increasing order** both row-wise and column-wise, count the number of negative numbers.  

### 💡 Approach  
- Traverse each row.  
- Count elements less than `0`.  
- Accumulate total count.  

### ⏱️ Complexity  
- **Time:** O(m × n) (brute-force)  
- **Space:** O(1)  

---

✅ **Day 12 Summary:**  
- Learned to find max difference with tracking minimum.  
- Practiced edge-to-edge distance finding in arrays.  
- Revised prime factor check for Ugly numbers.  
- Counted negatives in a sorted matrix with brute force.  
