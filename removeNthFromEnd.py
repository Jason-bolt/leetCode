# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        newList = []
        while current:
            newList.append(current.val)
            current = current.next

        print(newList)
        newList.pop(-n)
        print(newList)
       
        if len(newList) == 0:
            return ListNode('')

        newHead = ListNode(newList[0])
        head2 = newHead

        if len(newList) == 0:
            return ListNode()

        for i in range(len(newList)):
            newHead.val = newList[i]
            if i < len(newList) - 1:
                newHead.next = ListNode()
                newHead = newHead.next
        return head2