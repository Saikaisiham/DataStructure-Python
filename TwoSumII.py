from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0

        

        while l < r : 
            CurrentSum = numbers[l] + numbers[r]

            if CurrentSum > target : 
                r -= 1
            elif CurrentSum < target : 
                l += 1
            else :
                return  [l+1,r+1]
        return []


s = Solution()
print(s.twoSum([1,2,4,5,6], 3))
