# 📘 Day 10 Notes

## Problem 37: Minimum Number of Moves to Seat Everyone  
🔗 [LeetCode Link](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/)  

- **Approach**:
  - Sort both `seats` and `students`.
  - Match each student with the corresponding seat.
  - Calculate absolute differences and sum them.
- **Time Complexity**: `O(n log n)` (due to sorting)  
- **Space Complexity**: `O(1)`  

---

## Problem 38: Relative Sort Array  
🔗 [LeetCode Link](https://leetcode.com/problems/relative-sort-array/)  

- **Approach**:
  - First, iterate through `arr2` and collect matching elements from `arr1`.
  - Then, take remaining elements from `arr1` that are not in `arr2` and sort them.
  - Combine both parts.
- **Time Complexity**: `O(n * m + k log k)`  
  - `n = len(arr1), m = len(arr2), k = remaining elements`  
- **Space Complexity**: `O(n)`  

---

## Problem 39: Array Partition  
🔗 [LeetCode Link](https://leetcode.com/problems/array-partition/)  

- **Approach**:
  - Sort the array.
  - Take pairs `(nums[i], nums[i+1])`.
  - Add the minimum of each pair to the result.
- **Time Complexity**: `O(n log n)` (sorting dominates)  
- **Space Complexity**: `O(1)`  

---

## Problem 40: Missing Number  
🔗 [LeetCode Link](https://leetcode.com/problems/missing-number/)  

- **Approach**:
  - Create a list of numbers from `0` to `n`.
  - Compare with `nums` and return the missing one.
- **Time Complexity**: `O(n^2)` (because of `in` check inside loop).  
- **Space Complexity**: `O(n)`  

---

✅ **Day 10 Complete!**
