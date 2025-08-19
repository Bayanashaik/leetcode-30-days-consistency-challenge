# Problem 3: Defanging an IP Address
# LeetCode Link: https://leetcode.com/problems/defanging-an-ip-address/description/
# Description:
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every "." with "[.]".

class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for i in address:
            if i == ".":
                res += "[.]"
            else:
                res += i
        return res

# Example test
if __name__ == "__main__":
    sol = Solution()
    print(sol.defangIPaddr("1.1.1.1"))  # Expected output: "1[.]1[.]1[.]1"
