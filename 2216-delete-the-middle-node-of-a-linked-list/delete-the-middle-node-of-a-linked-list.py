# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast, prev = head, head, None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if slow == head and not slow.next: # only 1 iteam - delete it
            return None
        elif slow == head and not slow.next.next: # only 2 iteam - need to delete second one
            head.next = None
        else:
            prev.next = slow.next

        return head