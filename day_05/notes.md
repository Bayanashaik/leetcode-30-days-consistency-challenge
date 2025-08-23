# Day 05 Notes  

## Problem 17: Remove Element  
🔗 [Problem Link](https://leetcode.com/problems/remove-element/)  

- **Idea**: Use two pointers. Move all non-`val` elements to the front.  
- **Steps**:  
  1. Keep `index = 0`.  
  2. Loop through `nums`.  
  3. If element is not equal to `val`, assign it to `nums[index]` and increment `index`.  
  4. Return `index` as the new length.  
- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`  

---

## Problem 18: Height Checker  
🔗 [Problem Link](https://leetcode.com/problems/height-checker/)  

- **Idea**: Compare original heights with the sorted order.  
- **Steps**:  
  1. Make a copy of `heights` → `expected = sorted(heights)`.  
  2. Compare both lists index by index.  
  3. Count mismatches.  
- **Time Complexity**: `O(n log n)` (because of sorting).  
- **Space Complexity**: `O(n)` (for the `expected` list).  

---

## Problem 19: Coupon Code Validator  
🔗 [Problem Link](https://leetcode.com/problems/coupon-code-validator/)  

- **Idea**: Check conditions for valid coupons.  
- **Conditions**:  
  1. `businessLine` must be in allowed set `{electronics, grocery, pharmacy, restaurant}`.  
  2. `isActive[i]` must be `True`.  
  3. `code[i]` should contain only alphanumeric characters or `_`.  
- **Steps**:  
  1. Iterate through all coupons.  
  2. Validate each using conditions.  
  3. Append valid ones `(businessLine, code)` to a list.  
  4. Sort by `businessLine` and return only the `code`.  
- **Time Complexity**: `O(n log n)` (because of sorting).  
- **Space Complexity**: `O(n)`.  

---

## Problem 20: Remove Duplicates from Sorted Array  
🔗 [Problem Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)  

- **Idea**: Use two pointers. One pointer (`index`) tracks the position of unique elements.  
- **Steps**:  
  1. If list is empty → return 0.  
  2. Set `index = 1`.  
  3. Traverse from `i = 1` to `len(nums)-1`.  
  4. If `nums[i] != nums[i-1]`, place it at `nums[index]` and increment index.  
  5. Return `index` as new length.  
- **Time Complexity**: `O(n)`  
- **Space Complexity**: `O(1)`  

---

✅ **Summary**:  
- Practiced array manipulation (`Remove Element`, `Remove Duplicates`).  
- Practiced sorting + comparison (`Height Checker`).  
- Practiced condition-based validation (`Coupon Validator`).  
