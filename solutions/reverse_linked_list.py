# https://leetcode.com/problems/reverse-linked-list/submissions/1221320742/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        prev_node = None
        curr_node = head

        while curr_node:
            tail = ListNode(curr_node.val, tail)
            prev_node = curr_node
            curr_node = prev_node.next
        
        return tail