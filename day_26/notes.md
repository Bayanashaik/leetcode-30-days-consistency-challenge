# Day 26 Notes

## Problem 101: [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)
- **Idea**: Classic Fibonacci problem. To reach step `n`, you can come from step `n-1` or `n-2`.
- **Approach**: Use iterative DP with two variables (`a`, `b`) to save space.
- **Complexity**: O(n) time, O(1) space.

---

## Problem 102: [Length of Last Word](https://leetcode.com/problems/length-of-last-word/description/)
- **Idea**: Split string by spaces and return the length of the last word.
- **Approach**: Use Python `split()` and index the last element.
- **Complexity**: O(n) time, O(n) space.

---

## Problem 103: [Add Binary](https://leetcode.com/problems/add-binary/description/)
- **Idea**: Perform binary addition on two strings.
- **Approach**: Convert to integers with base 2, add, then convert back with `bin()`.
- **Complexity**: O(max(len(a), len(b))) time.

---

## Problem 104: [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)
- **Idea**: From range `1..n`, find numbers missing from the array.
- **Approach**: Use a set of input numbers and return elements not present.
- **Complexity**: O(n) time, O(n) space.
