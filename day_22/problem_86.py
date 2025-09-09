# Problem 86: Convert Date to Binary
# Link: https://leetcode.com/problems/convert-date-to-binary/

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = date.split('-')
        year = bin(int(date[0]))[2:]
        month = bin(int(date[1]))[2:]
        day = bin(int(date[-1]))[2:]
        return f"{year}-{month}-{day}"


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.convertDateToBinary("2023-12-31"))  # Expected: "11111100111-1100-11111"
    print(sol.convertDateToBinary("2000-01-01"))  # Expected: "11111010000-1-1"
