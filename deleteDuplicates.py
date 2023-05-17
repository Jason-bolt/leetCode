class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)

        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next