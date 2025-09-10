# Problem 92: Number of Segments in a String
# Link: https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution:
    def countSegments(self, s: str) -> int:
        s = s.split()
        count = 0
        for i in s:
            count += 1
        return count


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.countSegments("Hello, my name is John"))  # Expected: 5
    print(sol.countSegments("Hello"))                   # Expected: 1
    print(sol.countSegments("   "))                     # Expected: 0
