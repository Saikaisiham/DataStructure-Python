class Solution:
    """
    This code defines a class "Solution" with a method "searchInsert" that takes in a list of integers "nums" 
    and an integer "target". The method uses a binary search algorithm to find the index at which the "target" 
    should be inserted in the "nums" list such that it maintains the sorted order. 
    The method returns this index. If the "target" is already present in the "nums" list, 
    the method returns the index of the target in the list
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2

            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                l = mid + 1
            else :
                r = mid - 1
        return l

            