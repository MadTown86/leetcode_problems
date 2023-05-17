class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        # Copy initial head, remove next reference relace with None
        last_head = ListNode(head.val, None)
        head = head.next
        while head:
            new_pos = ListNode(head.val, last_head)
            last_head = new_pos
            head = head.next
        return last_head

if __name__ == "__main__":
    S = Solution()
    print(S.reverseList([]))