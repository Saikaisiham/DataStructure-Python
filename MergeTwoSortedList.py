class Solution:

    """
    This code is defining a class Solution and a method within it called mergeTwoLists. 
    The method takes in two inputs, list1 and list2, which are both of type Optional[ListNode]. 
    The method returns an output of type Optional[ListNode]. 
    The method creates a new ListNode called newNode, and another variable called tail which is set to newNode.
    It then enters a while loop that runs while both list1 and list2 are not None. 
    Within the while loop, it compares the value of the current nodes of list1 and list2 and assigns the smaller value to the next value of tail. 
    It then moves to the next node in the list that was used. 
    If one of the lists becomes empty, the remaining list is assigned to the next value of tail. 
    The method then returns newNode.next, which is the first element of the merged list
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode()
        tail = newNode

        while list1 and list2:
            if list1.val < list2.val :
                tail.next = list1
                list1 = list1.next
            else :
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2: 
            tail.next = list2
        return newNode.next