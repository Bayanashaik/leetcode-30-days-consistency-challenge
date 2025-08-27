from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        for i in range(len(arr)-1, -1, -1):
            new_val = max_right      # element to replace
            max_right = max(max_right, arr[i])  # update max
            arr[i] = new_val
        return arr


# -------------------- Test Cases --------------------
if __name__ == "__main__":
    s = Solution()
    print(s.replaceElements([17,18,5,4,6,1]))  # [18,6,6,6,1,-1]
    print(s.replaceElements([400]))            # [-1]
