from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if i != j and arr[i] == 2*arr[j]:
                    return True
        return False


# -------------------- Test Cases --------------------
if __name__ == "__main__":
    s = Solution()
    print(s.checkIfExist([10,2,5,3]))   # True
    print(s.checkIfExist([3,1,7,11]))   # False
    print(s.checkIfExist([-2,0,10,-19,4,6,-8])) # False
