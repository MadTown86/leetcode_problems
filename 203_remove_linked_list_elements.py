class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head.next is None:
            return head
        if head.

if __name__ == "__main__":
    T6 = ListNode(val=6)
    T5 = ListNode(val=5, next=T6)
    T4 = ListNode(val=5, next=T5)
    T3 = ListNode(val=4, next=T4)
    T2 = ListNode(val=3, next=T3)
    T1 = ListNode(val=2, next=T2)

    S = Solution()
    head = S.removeElements(T1, 5)

    while head.next is not None:
        print(head.val)
        head = head.next