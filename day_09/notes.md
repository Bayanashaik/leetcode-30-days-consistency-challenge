# Day 09 Notes

## Problem 33: [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/)
- For each number, count how many numbers are smaller.
- Time Complexity: O(n²)

---

## Problem 34: [Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/)
- Traverse from right to left.
- Keep track of maximum seen so far.
- Replace each element with max on its right.
- Time Complexity: O(n)

---

## Problem 35: [Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist/description/)
- Compare each element with double of others.
- Brute-force approach used.
- Time Complexity: O(n²)

---

## Problem 36: [Minimum Element After Replacement With Digit Sum](https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/)
- Replace each number with sum of its digits.
- Return the minimum digit sum.
- Time Complexity: O(n * m), where m is number of digits per number.
