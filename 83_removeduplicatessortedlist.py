"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        head_new = head
        while head and head.next:
            if head.val != head.next.val:
                head = head.next
            else:
                if head.next.next:
                    head.next = head.next.next
                else:
                    head.next = None
        return head_new

if __name__ == "__main__":
    N1 = ListNode(1)
    N2 = ListNode(1)
    N3 = ListNode(2)
    N1.next = N2
    N2.next = N3
    L1 = ListNode(1)
    L2 = ListNode(1)
    L3 = ListNode(2)
    L4 = ListNode(3)
    L5 = ListNode(3)
    L1.next = L2
    L2.next = L3
    L3.next = L4
    L4.next = L5
    S = Solution()
    hn = S.deleteDuplicates(N1)
    print(hn.val)
    while hn.next is not None:
        print(hn.next.val)
        hn = hn.next
    h2 = S.deleteDuplicates(L1)
    print(h2.val)
    while h2.next is not None:
        print(h2.next.val)
        h2 = h2.next


