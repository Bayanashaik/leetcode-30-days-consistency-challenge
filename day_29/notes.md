# Day 29 Notes

## Problem 113: Slowest Key
- **Link:** [Slowest Key](https://leetcode.com/problems/slowest-key/)
- **Idea:** Find the maximum key press duration.  
  If tie → take lexicographically larger key.
- **Approach:**  
  - Track time differences between consecutive releases.  
  - Update max duration and key accordingly.

---

## Problem 114: Count of Matches in Tournament
- **Link:** [Count of Matches in Tournament](https://leetcode.com/problems/count-of-matches-in-tournament/)
- **Idea:** Every round, teams are paired. Matches = `n//2`.  
- **Approach:**  
  - While teams remain, add matches.  
  - Update number of teams for next round.

---

## Problem 115: Kth Missing Positive Number
- **Link:** [Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)
- **Idea:** Generate missing numbers until `k` is reached.  
- **Approach:**  
  - Loop through numbers up to a limit (2000).  
  - Collect missing numbers not in `arr`.  
  - Return the `k-1` index.

---

## Problem 116: Three Consecutive Odds
- **Link:** [Three Consecutive Odds](https://leetcode.com/problems/three-consecutive-odds/)
- **Idea:** Find if there exists a subsequence of 3 consecutive odd numbers.  
- **Approach:**  
  - Iterate through array with sliding window of size 3.  
  - If all odd → return True.  
  - Otherwise False.

---
✅ Day 29 complete!
