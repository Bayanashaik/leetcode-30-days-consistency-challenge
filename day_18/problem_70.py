# Problem 70: String Matching in an Array
# Link: https://leetcode.com/problems/string-matching-in-an-array/

from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    res.add(words[i])
        return list(res)


# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.stringMatching(["mass","as","hero","superhero"]))  # ['as', 'hero']
    print(s.stringMatching(["leetcode","et","code"]))  # ['et', 'code']
    print(s.stringMatching(["blue","green","bu"]))  # []
