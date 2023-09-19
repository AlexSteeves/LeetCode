 

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def mergeSortedLists(self, list1, list2):
        final = ListNode()
        dummy = final
            
                
        while list1 and list2:

            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next

        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        return final.next
        
                
                