# Problem 53: Number of Students Doing Homework at a Given Time
# Link: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count  = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        return count


# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.busyStudent([1,2,3], [3,2,7], 4))   # 1
    print(s.busyStudent([4], [4], 4))           # 1
    print(s.busyStudent([4], [4], 5))           # 0
