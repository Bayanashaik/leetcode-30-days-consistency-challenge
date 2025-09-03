# Day 16 Notes

## Problem 61: Smallest Index With Equal Value
- **Link:** [Smallest Index With Equal Value](https://leetcode.com/problems/smallest-index-with-equal-value/description/)  
- Find the smallest index `i` where `i % 10 == nums[i]`.  
- If none found, return `-1`.  
- Approach:
  - Iterate through list
  - Track minimum valid index

---

## Problem 62: Find Target Indices After Sorting Array
- **Link:** [Find Target Indices After Sorting Array](https://leetcode.com/problems/find-target-indices-after-sorting-array/description/)  
- After sorting the array, return indices where elements equal `target`.  
- Approach:
  - Sort array
  - Collect indices matching target

---

## Problem 63: Find First Palindromic String in the Array
- **Link:** [Find First Palindromic String in the Array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/)  
- Return the first string that is a palindrome.  
- If none exist, return empty string.  
- Approach:
  - Iterate words
  - Check if `word == word[::-1]`

---

## Problem 64: Keep Multiplying Found Values by Two
- **Link:** [Keep Multiplying Found Values by Two](https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/)  
- Given `original`, if it's in array → double it, repeat until not found.  
- Approach:
  - Convert nums to set for O(1) lookup  
  - While loop to keep doubling

---
