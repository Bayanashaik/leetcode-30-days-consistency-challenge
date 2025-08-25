# Day 06 – LeetCode Problems Notes

---

## Problem 21: Move Zeroes
🔗 [Move Zeroes](https://leetcode.com/problems/move-zeroes/description/)

### Approach
- Use a pointer `index` to track the position where the next non-zero element should be placed.
- Traverse the array:
  - If the current element is non-zero, put it at `nums[index]` and increment `index`.
- After traversal, fill remaining positions with `0`.

### Complexity
- **Time:** O(n) – one pass to rearrange + one pass to fill zeros.
- **Space:** O(1) – in-place.

---

## Problem 22: Minimum Index Sum of Two Lists
🔗 [Minimum Index Sum of Two Lists](https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/)

### Approach
- Use two nested loops to check for common restaurants.
- Track the minimum index sum (`i + j`).
- If a new smaller sum is found → update result.
- If same sum appears again → add to result.

### Complexity
- **Time:** O(m × n) – where m = len(list1), n = len(list2).  
- **Space:** O(k) – output list (k = number of matches).

---

## Problem 23: Maximum Product of Three Numbers
🔗 [Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/description/)

### Approach
- Sort the array.
- The maximum product will be one of:
  - Product of the 3 largest numbers.
  - Product of the 2 smallest numbers (negative × negative) and the largest number.
- Return the maximum of these two.

### Complexity
- **Time:** O(n log n) – sorting.  
- **Space:** O(1) – in-place sort.

---

## Problem 24: Largest Number At Least Twice of Others
🔗 [Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/)

### Approach
- Find the maximum number and its index.
- Check if this maximum is at least **2 × every other number**.
- If condition fails → return `-1`.
- Else return index of max.

### Complexity
- **Time:** O(n) – scanning list.  
- **Space:** O(1).

---
