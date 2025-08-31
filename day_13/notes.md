# Day 13 Notes

## Problem 49: Element Appearing More Than 25% in Sorted Array
- **Link:** [LeetCode 1287](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/)
- **Approach:**  
  - Use a dictionary to count frequency of each element.
  - Track the element with maximum frequency.
- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)  
- **Learning:** Frequency maps are useful for quick counting.

---

## Problem 50: Find the Distance Value Between Two Arrays
- **Link:** [LeetCode 1385](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/)
- **Approach:**  
  - For each element in `arr1`, check if all differences with `arr2` are greater than `d`.  
  - If yes, increment count.
- **Time Complexity:** O(n*m)  
- **Space Complexity:** O(1)  
- **Learning:** Nested loops work fine when constraints are small.

---

## Problem 51: Minimum Value to Get Positive Step by Step Sum
- **Link:** [LeetCode 1413](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/)
- **Approach:**  
  - Maintain running sum.  
  - Track the minimum prefix sum.  
  - Answer = `-min_prefix_sum + 1`.
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Learning:** Prefix sum technique ensures we find the lowest dip.

---

## Problem 52: Kids With the Greatest Number of Candies
- **Link:** [LeetCode 1431](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)
- **Approach:**  
  - Find the maximum candy count.  
  - For each kid, check if `candies[i] + extraCandies >= max(candies)`.
- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)  
- **Learning:** Greedy check with max value simplifies the problem.

---

# Key Learnings
- Frequency maps help with majority/frequency problems.  
- Nested loops are fine for smaller constraints.  
- Prefix sums can be used to track minimum/maximum running totals.  
- Simple max-based checks are useful in greedy problems.  
