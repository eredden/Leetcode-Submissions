# https://leetcode.com/problems/merge-two-sorted-lists/submissions/1226176856/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        tail = temp

        # Compare values of both heads, add lower one to results.
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2     = list2.next
            else:
                tail.next = list1
                list1     = list1.next

            tail = tail.next
            
        # Get the remaining items from the larger linked list.
        if not list1:
            tail.next = list2
        else:
            tail.next = list1

        return temp.next
