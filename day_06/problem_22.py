# Problem: Minimum Index Sum of Two Lists
# Link: https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# Description: Find the common restaurants with the least index sum between two string lists.

from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_v = float('inf')
        output = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j < min_v:
                        min_v = i + j
                        output = [list1[i]]
                    elif i + j == min_v:
                        output.append(list1[i])
        return output

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
