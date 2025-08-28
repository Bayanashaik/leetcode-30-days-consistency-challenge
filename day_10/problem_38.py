from typing import List

class Solution: 
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    result.append(arr1[j])
        remaining = []
        for j in arr1:
            if j not in arr2:
                remaining.append(j)
        result.extend(sorted(remaining))
        return result


# ✅ Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))  
    # Expected [2,2,2,1,4,3,3,9,6,7,19]
    print(s.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))  
    # Expected [22,28,8,6,17,44]
