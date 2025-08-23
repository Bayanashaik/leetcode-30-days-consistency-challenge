# Problem 19: Coupon Code Validator
# Link: https://leetcode.com/problems/coupon-code-validator/

from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        output = []
        allowed = {"electronics", "grocery", "pharmacy", "restaurant"}

        for i in range(len(code)):
            if code[i] and businessLine[i] in allowed and isActive[i]:
                if all(ch.isalnum() or ch == '_' for ch in code[i]):
                    output.append((businessLine[i], code[i]))

        output.sort()
        return [c for _, c in output]

# Example Test
if __name__ == "__main__":
    sol = Solution()
    codes = ["ABC_123", "DISCOUNT", "INVALID!"]
    business = ["electronics", "grocery", "pharmacy"]
    active = [True, True, False]
    print(sol.validateCoupons(codes, business, active))  # Output: ['ABC_123', 'DISCOUNT']
