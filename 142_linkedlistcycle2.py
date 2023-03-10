from typing import Self

class ListNode:
    def __init__(self, x, next: Self = None):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        bins = []
        if not head or not head.next or head.next is head:
            return head
        bins.append(head)
        while head.next:
            for x in bins:
                print(x)
            if head.next in bins:
                return head.next
            else:
                bins.append(head.next)
                head = head.next
        return bins[0]

if __name__ == '__main__':
    N1 = ListNode(1)
    N2 = ListNode(2)
    N3 = ListNode(8)
    N4 = ListNode(10)
    N3.next = N4
    N2.next = N3
    N1.next = N2
    N4.next = N1

    S = Solution()
    print(f'THE ONE FOUND: {S.detectCycle(N1)}')
