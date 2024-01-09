#https://leetcode.com/problems/odd-even-linked-list/

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # o-> odd pointer / e -> even pointer / heade even head pointer
        o, e, heade = head, head.next, head.next

        while e and e.next:
            o.next = o.next.next
            e.next = e.next.next
            o = o.next
            e = e.next

        # link up the last odd node to the first even node
        o.next = heade

        return head