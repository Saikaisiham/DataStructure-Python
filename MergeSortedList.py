class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n -1

        # last is a variable used to keep track of the current end position of the merged array.
        # Initially, last is set to m + n - 1, which is the index of the last element in nums1 after the two arrays have been merged. 
        # As the code iterates over the elements in nums1 and nums2, it compares the elements and 
        # places the larger of the two at the end of nums1 (that is, at the index last).
        # After each comparison, the value of last is decremented by 1 to move the end of the merged 
        # array one position to the left, until all elements from both nums1 and nums2 have been merged into nums1.

        while m > 0 and n > 0 : 
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else :
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        while n > 0 : 
            nums1[last] = nums2[n - 1]
            n , last = n - 1 , last - 1



# m and n are the lengths of the two arrays nums1 and nums2 that are being merged. These lengths determine the number
# of elements in each array and are used in the merging process to iterate over the elements in the correct order.
# hat only the first 3 elements of nums1 should be considered during the merging process.



# The reason m-1 is used instead of n-1 is because the elements in nums1 are being compared with the elements in nums2 to 
# determine which one should be placed at the end of nums1.

# Since the arrays are sorted, the largest elements are placed at the end of the arrays. By using m-1 instead of n-1, the code is 
# accessing the last element in nums1 that contains a valid value (that is, the element with an index m-1),
#  and comparing it with the last element in nums2 (that is, the element with an index n-1).

# This is done because m represents the number of valid elements in nums1, and m-1 is the index of the last valid element in 
# nums1. By comparing these elements, the code can determine which element should be placed at the end of nums1 (that is, at the
#  index last, which is equal to m + n - 1).
