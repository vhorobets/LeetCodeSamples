# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # s = set()

        # p1 = headA
        # while p1:
        #     s.add(p1)
        #     p1 = p1.next

        # p2 = headB
        # while p2:
        #     if p2 in s:
        #         return p2

        #     p2 = p2.next

        # return None

        # a1 - a2 - a3 - c1 - c2 - b1 - b2 - b3 - b4 - c1
        # b1 - b2 - b3 - b4 - c1 - c2 - a1 - a2 - a3 - c1

        p1, p2 = headA, headB

        while p1 != p2:
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next

            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next

        return p1




        