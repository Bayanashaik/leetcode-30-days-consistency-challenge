# 📘 Day 30 – Notes

## 🔹 Problem 117: Add Digits  
**Link:** [Add Digits](https://leetcode.com/problems/add-digits/description/)  
**Concepts Used:** Digital Root, Modular Arithmetic  
- Instead of repeatedly summing digits, we use the **digital root formula**.  
- If `num == 0 → return 0`.  
- If `num % 9 == 0 → return 9`.  
- Otherwise → `num % 9`.  
- Runs in **O(1)** time.  

---

## 🔹 Problem 118: Add Strings  
**Link:** [Add Strings](https://leetcode.com/problems/add-strings/description/)  
**Concepts Used:** String Manipulation, Big Integer Handling  
- We simulate adding two large numbers given as strings.  
- Instead of manual digit-by-digit addition, here the solution uses **Python’s big int** capability (`int(num1) + int(num2)`).  
  

---

## 🔹 Problem 119: Maximize Sum of Array After K Negations  
**Link:** [Maximize Sum of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/)  
**Concepts Used:** Sorting, Greedy  
- Sort numbers.  
- Flip as many negative numbers as possible until `k` runs out.  
- If `k` is still > 0 and odd, flip the smallest number.  
- Finally, sum the array.  
- Time complexity: **O(n log n)** due to sorting.  

---

## 🔹 Problem 120: Minimum Time Visiting All Points  
**Link:** [Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/description/)  
**Concepts Used:** Geometry, Math  
- To move between two points `(x1, y1)` and `(x2, y2)` →  
  - Time needed = `max(|x2 - x1|, |y2 - y1|)` (because you can move diagonally).  
- Sum this for all consecutive pairs of points.  
- Runs in **O(n)** time.  

---

🥳 I’ve successfully completed 30 days of coding challenge and solved 120 problems consistently. 🚀
