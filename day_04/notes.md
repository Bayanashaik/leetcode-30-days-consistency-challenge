# Day 04 Notes

## Problem 13: Best Time to Buy and Sell Stock
- **LeetCode Link:** [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- **Problem Description:**  
  You are given an array where each element represents the price of a stock on that day.  
  You need to maximize your profit by choosing a day to buy and a later day to sell.
- **Approach / Algorithm:**  
  Track the minimum price so far, and calculate the maximum profit by checking the difference with the current price.
- **Key Learning:**  
  - Use `float('inf')` for initial min value.  
  - Update min price when a lower price is found.  
  - Update max profit whenever current profit is larger.

---

## Problem 14: Contains Duplicate
- **LeetCode Link:** [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)
- **Problem Description:**  
  Given an integer array, return `true` if any value appears more than once, otherwise return `false`.
- **Approach / Algorithm:**  
  Use a dictionary (hash map) to keep track of seen numbers. If a number repeats, return `True`.
- **Key Learning:**  
  - Dictionary (hash map) provides O(1) average lookup.  
  - Fast duplicate detection using set or map.  

---

## Problem 15: Merge Sorted Array
- **LeetCode Link:** [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/)
- **Problem Description:**  
  You are given two sorted arrays `nums1` and `nums2`, and you must merge them into `nums1` in sorted order.  
- **Approach / Algorithm:**  
  - Slice the first `m` elements of `nums1`.  
  - Merge with `nums2`.  
  - Use Python’s built-in `sorted()` to sort and store back into `nums1`.  
- **Key Learning:**  
  - In-place array modification using `nums1[:]`.  
  - Merging and sorting arrays efficiently.

---

## Problem 16: Plus One
- **LeetCode Link:** [Plus One](https://leetcode.com/problems/plus-one/description/)
- **Problem Description:**  
  Given a non-empty array of digits representing a non-negative integer, increment the integer by one.  
- **Approach / Algorithm:**  
  - Start from the last digit.  
  - If it’s less than 9, just add one and return.  
  - If it’s 9, set it to 0 and carry over to the next digit.  
  - If all digits were 9, prepend `1`.  
- **Key Learning:**  
  - Carry propagation logic.  
  - Edge cases like `[9,9] → [1,0,0]`.  
