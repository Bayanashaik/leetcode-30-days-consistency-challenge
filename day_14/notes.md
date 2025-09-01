# Day 14 - LeetCode Problems Notes

## Problem 53: Number of Students Doing Homework at a Given Time
- **Link**: [LeetCode 1450](https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/)
- **Concept**: Iterate over all students and check if `queryTime` is between `startTime[i]` and `endTime[i]`.
- **Key Point**: Simple range checking.
- **Time Complexity**: O(n)

---

## Problem 54: Distribute Candies
- **Link**: [LeetCode 575](https://leetcode.com/problems/distribute-candies/)
- **Concept**: 
  - You can only eat half of the candies.
  - Unique types are limited by `len(set(candyType))`.
  - Answer is the minimum of these two values.
- **Time Complexity**: O(n)

---

## Problem 55: Sort Array By Parity
- **Link**: [LeetCode 905](https://leetcode.com/problems/sort-array-by-parity/)
- **Concept**: 
  - Collect even numbers first, then odd numbers.
  - Return concatenation of two lists.
- **Time Complexity**: O(n)

---

## Problem 56: Smallest Range I
- **Link**: [LeetCode 908](https://leetcode.com/problems/smallest-range-i/)
- **Concept**: 
  - Range after adding/subtracting `k` is `(max(nums) - k) - (min(nums) + k)`.
  - If result < 0, answer is 0 (because range cannot be negative).
- **Time Complexity**: O(n)
