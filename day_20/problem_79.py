# Problem 79: Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        other = ['','','','','','']
        res = ""
        for i in s:
            if i.isalnum():
                res += i

        o = ""
        for i in res:
            if i.isupper():
                o += i.lower()
            else:
                o += i

        if o == o[::-1]:
            return True    
        else:
            return False            


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Expected: True
    print(sol.isPalindrome("race a car"))  # Expected: False
    print(sol.isPalindrome(" "))  # Expected: True
