# https://leetcode.com/problems/remove-linked-list-elements/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        while head.val == val and head.next:
            next_pos = head.next
            head.next = None
            head = next_pos
        if head.val == val:
            return None
        if head and head.next and head.next.next:
            last_pos = head
            cursor = last_pos.next
            next_pos = cursor.next
            while next_pos:
                if cursor.val == val:
                    last_pos.next = next_pos
                    cursor = next_pos
                    next_pos = cursor.next
                else:
                    last_pos = cursor
                    cursor = next_pos
                    next_pos = cursor.next
            if cursor.val == val:
                last_pos.next = None
            return head
        else:
            if head and not head.next:
                if head.val != val:
                    return head
                else:
                    return None
            elif head.next.val == val:
                head.next = None
                return head
            else:
                return head

# I didn't think to create a 'dummy' sentinel node.  Dang, much easier answer I am goign to use the next time.
class Solution2:
    def removeElements2(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev, node = dummy, head

        while node:
            if node.val == val:
                prev.next = node.next
            else:
                prev = node
            node = node.next

        return dummy.next





if __name__ == "__main__":
    T7 = ListNode(val=6)
    T6 = ListNode(val=5, next=T7)
    T5 = ListNode(val=4, next=T6)
    T4 = ListNode(val=3, next=T5)
    T3 = ListNode(val=6, next=T4)
    T2 = ListNode(val=2, next=T3)
    T1 = ListNode(val=1, next=T2)

    S4 = ListNode(val=7)
    S3 = ListNode(val=7, next=S4)
    S2 = ListNode(val=7, next=S3)
    S1 = ListNode(val=7, next=S2)

    SS1 = ListNode(val=8)

    L1 = ListNode()

    S = Solution()
    T = S.removeElements(T1, 6)
    if not T:
        print([])
    else:
        while T and T.next:
            print(T.val)
            T = T.next
        print(T.val)