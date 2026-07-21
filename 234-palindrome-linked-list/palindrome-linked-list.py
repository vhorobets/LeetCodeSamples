# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            # Odd number of nodes: slow is the middle node.
            slow = slow.next

        second_half_head = self.__reverse_list(slow)

        p1, p2 = head, second_half_head

        while p1 and p2:
            if p1.val != p2.val:
                return False

            p1 = p1.next
            p2 = p2.next

        return True


    def __reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev