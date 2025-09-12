# Problem 97: Vowels Game in a String
# Link: https://leetcode.com/problems/vowels-game-in-a-string/

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 'aeiou'
        for i in s:
            if i in vowels:
                return True
        return False


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.doesAliceWin("abc"))   # Expected: True (contains 'a')
    print(sol.doesAliceWin("xyz"))   # Expected: False
    print(sol.doesAliceWin("ou"))    # Expected: True
