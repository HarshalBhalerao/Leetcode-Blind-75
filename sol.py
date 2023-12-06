# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy

        # while list 1 and list2 are not null or not empty
        while list1 and list2:
            if list1.val < list2.val:
                # get the element from list1 and assign it to the head of the dummy list
                head.next = list1
                list1 = list1.next
            else:
                # get the element from list2 and assign it to the head of the dummy list
                head.next = list2
                list2 = list2.next
            
            # Once the element is added we update the position of our head
            head = head.next

        # if either list1 or list 2 is empty, then we look for which list isn't and add that to our merged sorted array as the rest of its elements would be in sorted order
        if list1:
            head.next = list1
        else: 
            head.next = list2

        return dummy.next
