# Problem 103: Add Binary
# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = int(a, 2) + int(b, 2)
        return bin(res)[2:]


# ✅ Test Cases
s = Solution()
print(s.addBinary("11", "1"))   # "100"
print(s.addBinary("1010", "1011"))  # "10101"
print(s.addBinary("0", "0"))    # "0"
