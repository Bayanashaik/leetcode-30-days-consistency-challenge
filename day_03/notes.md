# Day 03 Notes

## Problem 9: Check if Any Element Has Prime Frequency
- **LeetCode Link:** [Check if Any Element Has Prime Frequency](https://leetcode.com/problems/check-if-any-element-has-prime-frequency/description/)
- **Problem Description:**  
  Given an integer array, check if the frequency of any element is a prime number.  
  Return `True` if such an element exists, otherwise `False`.
- **Approach / Algorithm:**  
  1. Use a dictionary to count frequency of each element.  
  2. For each frequency, check if it is a prime number.  
  3. If any prime frequency exists → return `True`. Else return `False`.  
- **Key Learning:**  
  - Counting frequencies with dictionary.  
  - Implementing prime number check.  
  - Early exit when condition is satisfied.

---

## Problem 10: Third Maximum Number
- **LeetCode Link:** [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/description/)
- **Problem Description:**  
  Return the third distinct maximum number in the array.  
  If it does not exist, return the maximum number.  
- **Approach / Algorithm:**  
  1. Convert array to `set` to remove duplicates.  
  2. Sort unique numbers in descending order.  
  3. If there are at least 3 numbers → return the 3rd maximum.  
     Otherwise → return the maximum.  
- **Key Learning:**  
  - Removing duplicates using `set()`.  
  - Sorting in descending order.  
  - Handling conditional return values.

---

## Problem 11: Majority Element
- **LeetCode Link:** [Majority Element](https://leetcode.com/problems/majority-element/description/)
- **Problem Description:**  
  Find the element that appears more than `n/2` times in the array.  
  It is guaranteed to exist.  
- **Approach / Algorithm:**  
  1. Count occurrences of each element using dictionary.  
  2. Return the element whose count > n/2.  
  *(Alternative: Boyer-Moore Voting Algorithm in O(n), O(1) space)*  
- **Key Learning:**  
  - Frequency counting approach.  
  - Understanding the majority element property.  
  - Optimized Boyer-Moore algorithm.

---

## Problem 12: Single Number
- **LeetCode Link:** [Single Number](https://leetcode.com/problems/single-number/description/)
- **Problem Description:**  
  Every element appears twice except for one element which appears once.  
  Find and return that single element.  
- **Approach / Algorithm:**  
  1. Count frequencies using dictionary.  
  2. Return the element with count = 1.  
  *(Alternative: XOR approach → `ans = 0; for num in nums: ans ^= num`)*  
- **Key Learning:**  
  - Using dictionary to count frequencies.  
  - Identifying unique elements.  
  - XOR property for optimized solution.
