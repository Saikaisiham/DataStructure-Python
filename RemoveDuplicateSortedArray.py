from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1,len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l


nums = [1, 1, 2, 2, 3, 4, 4, 5]
solution = Solution()
length = solution.removeDuplicates(nums)

print("Modified list:", nums[:length])
print("Length of modified list:", length)