class Solution:
    """This class contains a method called 'containsDuplicate' which accepts a list 
of integers as input and returns a boolean indicating whether or not the list 
contains any duplicate values. The method uses a dictionary to keep track of the 
elements in the list and returns True if any element is found to be a duplicate"""
    def containsDuplicate(self, nums: List[int]) -> bool:   
        d = {}

        for i in nums :
            if i in d:
                return True
            d[i] = 1

        return False
