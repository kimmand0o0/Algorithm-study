#https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)

        front = head.next
        front.next = head

        head.next = None

        return new_head