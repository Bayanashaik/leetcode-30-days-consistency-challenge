# Problem 8: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Approach: Use a stack to check if every opening bracket has a matching closing one
# Key learning: Stack-based validation for parentheses matching

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if top == pairs[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

# Example test
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))     # Output: True
    print(sol.isValid("()[]{}")) # Output: True
    print(sol.isValid("(]"))     # Output: False
    print(sol.isValid("([)]"))   # Output: False
    print(sol.isValid("{[]}"))   # Output: True
