class Solution:
    
    """This code defines a class "Solution" that contains a method "twoSum". The method takes in two arguments, "nums" which is a list of integers and "target" which is an integer. The method returns a list of integers.
    The method uses a hashmap(dictionary) to store the value and index of each element in the array. 
    It then iterates through the array, checking if the difference between the target and the current element 
    is already in the hashmap. If it is, it returns the indices of the current element and the element found 
    in the hashmap, which are the indices of the two 
    elements that add up to the target. If no such pair is found, the method returns nothing"""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} #index,val
        for i , n in enumerate(nums):
            diff = target - n
            if diff in map :
                return [map[diff],i]

            map[n]=i
        return