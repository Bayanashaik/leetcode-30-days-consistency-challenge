# Problem: Minimum Index Sum of Two Lists
# Link: https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# Description: Find the common restaurants with the least index sum between two string lists.

from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {v: i for i, v in enumerate(list1)}
        min_sum = float('inf')
        result = []
        for j, v in enumerate(list2):
            if v in index_map:
                s = j + index_map[v]
                if s < min_sum:
                    min_sum = s
                    result = [v]
                elif s == min_sum:
                    result.append(v)
        return result

# Test Cases
s = Solution()
print(s.findRestaurant(
    ["Shogun","Tapioca Express","Burger King","KFC"],
    ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
))  # ["Shogun"]

print(s.findRestaurant(
    ["Shogun","Tapioca Express","Burger King","KFC"],
    ["KFC","Shogun","Burger King"]
))  # ["Shogun"]

print(s.findRestaurant(["A","B","C"], ["C","B","A"]))  # ["A","B","C"]
print(s.findRestaurant(["A"], ["A"]))  # ["A"]
print(s.findRestaurant(["A","B"], ["C","D"]))  # []
