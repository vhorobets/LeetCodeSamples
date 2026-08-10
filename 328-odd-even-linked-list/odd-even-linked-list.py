# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        cnt = 1

        #find tail & count of items
        while tail and tail.next:
            tail = tail.next
            cnt += 1

        if not head or cnt == 1:
            return head


        #we need to remove even node and add it to the tail
        current_even = head.next
        current_count = 2
        prev = head
        while current_even.next and current_count <= cnt:
            prev.next = current_even.next
            prev = prev.next
            tail.next = current_even
            tail = tail.next
            tail.next = None
            current_even = prev.next
            current_count += 2


        return head
    