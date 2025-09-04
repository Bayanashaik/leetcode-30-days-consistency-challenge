# Day 17 Notes

## Problem 65: Reverse Integer
- **Link:** [Reverse Integer](https://leetcode.com/problems/reverse-integer/)
- Convert integer to string, reverse it, and handle negative numbers separately.
- Convert back to integer and check if it lies within 32-bit signed range.
- If overflow → return 0.
- **Key Concept:** String manipulation, integer overflow check.

---

## Problem 66: Count Hills and Valleys in an Array
- **Link:** [Count Hills and Valleys in an Array](https://leetcode.com/problems/count-hills-and-valleys-in-an-array/)
- Remove adjacent duplicates first.
- A **hill**: number greater than neighbors.
- A **valley**: number smaller than neighbors.
- Traverse array and count hills + valleys.
- **Key Concept:** Preprocessing duplicates, local extrema.

---

## Problem 67: Next Greater Element I
- **Link:** [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
- For each element in `nums1`, find it in `nums2`.
- From that position, look for the next greater element.
- If none found → `-1`.
- **Key Concept:** Nested loops, next greater element.

---

## Problem 68: Check If It Is a Straight Line
- **Link:** [Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)
- Given coordinates, check if all points lie on the same line.
- Use cross product formula:
  - `(x1-x0)*(y-y1) == (x-x1)*(y1-y0)`
- If true for all points → straight line.
- **Key Concept:** Geometry, slope comparison with cross product.
