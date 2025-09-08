# Problem 83: Minimum Number of Chairs in a Waiting Room
# Link: https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        max_ = 0
        for i in s:
            if i == 'E':
                count += 1
                max_ = max(max_, count)
            else:
                count -= 1
        return max_


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumChairs("EEEE"))       # Expected: 4
    print(sol.minimumChairs("EELEEL"))     # Expected: 2
    print(sol.minimumChairs("ELEELE"))     # Expected: 2
