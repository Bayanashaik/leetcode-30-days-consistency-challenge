okay i have completed day_17 four problems give problem files without changing my code and add test cases and also give me notes file also for problem_65   https://leetcode.com/problems/reverse-integer/description/  code 
               class Solution:
    def reverse(self, x: int) -> int:
        nums = str(x)
        
        if nums[0] == '-':
            res = '-'+nums[:0:-1]
        else:
            res = nums[::-1]
        reversed_num = int(res)
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num 
         problem_66 https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/  code 
         class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                arr.append(nums[i])
        
        hv_count = 0
        for i in range(1, len(arr)-1):
                
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                hv_count += 1
            elif arr[i]<arr[i-1] and arr[i]<arr[i+1]:
                hv_count += 1
        return hv_count 
            
         
            problem_67 https://leetcode.com/problems/next-greater-element-i/description/  code  class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                        nex = -1
                        for k in range(j+1, len(nums2)):
                            if nums2[k]>nums1[i]:                       
                                nex = (nums2[k])
                                break
                            
                        ans.append(nex)
                        break
                    
                        
        return ans           
              
           

       problem_68 https://leetcode.com/problems/check-if-it-is-a-straight-line/description/ code class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0,y0),(x1,y1) = coordinates[:2]
        for x, y in coordinates:
            if (x1-x0)*(y-y1) != (x-x1)*(y1-y0):
                return False
        return True 