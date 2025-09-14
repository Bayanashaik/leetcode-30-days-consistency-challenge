# Day 27 Notes

## Problem 105: H-Index
🔗 [Link](https://leetcode.com/problems/h-index/)  
- **Approach**: Sort citations in descending order. Count how many papers have at least `i+1` citations.  
- **Key Point**: Classic greedy + sorting problem.  
- **Complexity**: O(n log n).

---

## Problem 106: Maximum Ice Cream Bars
🔗 [Link](https://leetcode.com/problems/maximum-ice-cream-bars/)  
- **Approach**: Sort costs, then greedily buy until coins run out.  
- **Key Point**: Greedy strategy works since we should always buy cheaper ice creams first.  
- **Complexity**: O(n log n).

---

## Problem 107: Sort Characters By Frequency
🔗 [Link](https://leetcode.com/problems/sort-characters-by-frequency/)  
- **Approach**: Count frequency of each character → sort by frequency → rebuild string.  
- **Key Point**: Dictionary + sorting by frequency.  
- **Complexity**: O(n log n).

---

## Problem 108: Majority Element II
🔗 [Link](https://leetcode.com/problems/majority-element-ii/)  
- **Approach**: Count frequency of each element → add if count > n/3.  
- **Key Point**: Direct dictionary counting approach. (Can also be solved with Boyer-Moore Voting algorithm).  
- **Complexity**: O(n).
