# Day 15 Notes

## Problem 57: Valid Mountain Array
- **Link:** [Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/description/)  
- An array is a valid mountain if:
  - It strictly increases to a peak
  - Then strictly decreases after the peak
  - Peak cannot be first or last element  
- Approach:  
  - Find the peak (max element index)  
  - Check strictly increasing before peak  
  - Check strictly decreasing after peak  

---

## Problem 58: Maximum Product of Two Elements in an Array
- **Link:** [Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/)  
- We need to maximize `(a-1) * (b-1)` where `a` and `b` are two largest elements.  
- Approach:  
  - Sort the array  
  - Take last two elements → `(nums[-1]-1)*(nums[-2]-1)`  

---

## Problem 59: Concatenation of Array
- **Link:** [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/description/)  
- Given `nums`, return `nums + nums`.  
- Approach:  
  - Use `nums[:] + nums[:]` to create the concatenated array.  

---

## Problem 60: Count Number of Pairs With Absolute Difference K
- **Link:** [Count Number of Pairs With Absolute Difference K](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/)  
- Count pairs `(i, j)` such that `|nums[i] - nums[j]| == k`.  
- Approach:  
  - Use nested loops to check each pair  
  - Increment counter when condition matches  

---
