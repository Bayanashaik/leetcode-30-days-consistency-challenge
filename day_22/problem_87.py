# Problem 87: Find the Original Typed String I
# Link: https://leetcode.com/problems/find-the-original-typed-string-i/

class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        for i in range(1, len(word)):
            if word[i-1] == word[i]:
                count += 1
        return count


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.possibleStringCount("abbccc"))  # Expected: 4 (bb + cc + c)
    print(sol.possibleStringCount("aaaa"))    # Expected: 4
    print(sol.possibleStringCount("abc"))     # Expected: 1
