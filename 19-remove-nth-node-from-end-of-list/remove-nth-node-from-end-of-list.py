# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, p2, prev = head, head, None

        cnt = 0
        while p1:
            p1 = p1.next
            cnt += 1
            if cnt > n:
                prev = p2
                p2 = p2.next

        if cnt == n:
            return head.next
        
        prev.next = p2.next

        return head