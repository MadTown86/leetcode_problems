#https://leetcode.com/problems/intersection-of-two-linked-lists/
import numpy as np
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from collections import deque
class Solution:
    a = deque()
    b = deque()
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headA:
            self.a.appendleft(headA)
            headA = headA.next
        while headB:
            self.b.appendleft(headB)
            headB = headB.next
        ab = self.a + self.b
        ba = self.b + self.a

        x, y = 0, len(ab)-1
        while x <= len(ab)-1:
            if ab[x] == ab[y]:
                return ab[x]
            x += 1
            y -= 1

        return ab[x]


# https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/1092898/JS-Python-Java-C%2B%2B-or-Easy-O(1)-Extra-Space-Solution-w-Visual-Explanation
"""
Learning Experience with this one.  I need to remember this traversal concept.

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while (a != b):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
"""




class Solution2:
    vp1 = []
    vp2 = []

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        count = 0
        while headA and headB:
            if headA.val == self.vp2 and headA.next.val in self.vp2:
                return headA
            elif headB.val in self.vp1 and headB.next.val in self.vp1:
                return headB
            else:
                self.vp1.append(headA.val)
                self.vp2.append(headB.val)
                headA = headA.next
                headB = headB.next
                count += 1

        while headA:
            if headA.val in self.vp2 and headA.next.val in self.vp2:
                return headA
            else:
                self.vp1.append(headA.val)
                headA = headA.next

        while headB:
            if headB.val in self.vp1 and headB.next.val in self.vp1:
                return headB
            else:
                self.vp2.append(headB.val)
                headB = headB.next





if __name__ == "__main__":
    N1 = ListNode(1)
    N2 = ListNode(2)
    N3 = ListNode(3)
    N4 = ListNode(4)
    N5 = ListNode(5)
    N1.next = N2
    N2.next = N3
    N3.next = N4
    N4.next = N5

    L1 = ListNode(6)
    L2 = ListNode(7)
    L1.next = L2
    L2.next = N3

    S = Solution()
    print(S.getIntersectionNode(L1, N1))
