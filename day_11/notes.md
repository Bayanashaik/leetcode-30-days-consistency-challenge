# 📘 Day_11 Notes

---

## 🔹 Problem 41: Contains Duplicate II
🔗 [Problem Link](https://leetcode.com/problems/contains-duplicate-ii/)

### Approach: Hash Map (Dictionary)
- Use a dictionary `seen` to store the **last index** of each number.
- While traversing the array, check:
  - If the number already exists in `seen` **and** the index difference `<= k` → return `True`.
  - Else, update the number’s index in `seen`.
- If no such pair is found, return `False`.

✅ Efficient: **O(n)** time, **O(n)** space.

---

## 🔹 Problem 42: Intersection of Two Arrays
🔗 [Problem Link](https://leetcode.com/problems/intersection-of-two-arrays/)

### Approach: Sets
- Convert both arrays into sets → removes duplicates.
- Compare elements of the two sets:
  - If `i == j`, add it to result list.
- Return the result list (unique intersection values).

✅ Time: **O(n × m)** (due to nested loop, but sets reduce size).
✅ Can be optimized with `set1 & set2`.

---

## 🔹 Problem 43: 1-bit and 2-bit Characters
🔗 [Problem Link](https://leetcode.com/problems/1-bit-and-2-bit-characters/)

### Approach: Greedy Traversal
- Iterate over the `bits` array:
  - If the current bit is `1` → move `i += 2` (represents a 2-bit character).
  - Else → move `i += 1`.
- At the end, check if the pointer `i` stops exactly at the **last bit** → return `True`.
- Else return `False`.

✅ Time: **O(n)**, Space: **O(1)**.

---

## 🔹 Problem 44: Squares of a Sorted Array
🔗 [Problem Link](https://leetcode.com/problems/squares-of-a-sorted-array/)

### Approach: Square + Sort
- Traverse the array and compute the **square of each element**.
- Store in a result list `res`.
- Sort the list and return.

✅ Time: **O(n log n)** (due to sorting).
✅ Space: **O(n)**.
💡 Can be optimized with **two-pointer approach** to achieve **O(n)**.

---

📅 **Summary of Day_11**
- Learned to use **Hash Maps** for duplicate checking with index differences.
- Practiced **Set operations** for array intersections.
- Understood **bit pattern traversal** for 1-bit/2-bit characters.
- Applied **sorting with transformation** for array problems.