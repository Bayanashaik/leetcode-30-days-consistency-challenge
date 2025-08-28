from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        sum = 0
        for i in range(len(seats)):
            diff = abs(seats[i]-students[i])
            sum = sum + diff
        return sum


# ✅ Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.minMovesToSeat([3,1,5], [2,7,4]))  # Expected 4
    print(s.minMovesToSeat([4,1,5,9], [1,3,2,6]))  # Expected 7
    print(s.minMovesToSeat([2,2,6,6], [1,3,2,6]))  # Expected 4
