# Problem 84: Count the Number of Special Characters I
# Link: https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = ''
        out = ''
        for i in word:
            if i.islower():
                res += i
            else:
                out += i.lower()
        count = 0
        out = list(set(out))
        for i in out:
            if i in res:
                count += 1
        return count


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfSpecialChars("aaAbcBC"))   # Expected: 3 (a, b, c)
    print(sol.numberOfSpecialChars("abc"))       # Expected: 0
    print(sol.numberOfSpecialChars("abC"))       # Expected: 1
