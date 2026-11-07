# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverseList(head)

        has_one = False
        current = head

        while current:
            doubled_value = current.val * 2
            if has_one:
                doubled_value += 1

            if doubled_value > 9:
                current.val = doubled_value % 10
                has_one = True
            else:
                current.val = doubled_value
                has_one = False

            if not current.next:
                break
            else:
                current = current.next

        if has_one:
            current.next = ListNode(1)

        return self.reverseList(head)


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev