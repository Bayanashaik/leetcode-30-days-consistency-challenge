# Problem 7: Roman to Integer
# Link: https://leetcode.com/problems/roman-to-integer/description/
# Approach: Map Roman numerals to integers, handle subtraction cases
# Key learning: Use dictionary mapping and conditional subtraction logic

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and roman_to_num[s[i]] < roman_to_num[s[i+1]]:
                total += roman_to_num[s[i+1]] - roman_to_num[s[i]]
                i += 2
            else:
                total += roman_to_num[s[i]]
                i += 1
        return total

# Example test
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))     # Output: 3
    print(sol.romanToInt("LVIII"))   # Output: 58
    print(sol.romanToInt("MCMXCIV")) # Output: 1994
