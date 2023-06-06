# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        front_c = 0
        back_c = 0
        if head and not head.next:
            return True
        if head and head.next and not head.next.next:
            if head.val == head.next.val:
                return True
            return False
        while head and head.next and head.next.next:
            print(head.val, head.next.val, head.next.next.val)
            if head.val <= head.next.val <= head.next.next.val:
                front_c += 1
            if head.val >= head.next.val >= head.next.next.val:
                back_c += 1
            head = head.next
            print(front_c, back_c)
            input()

        return front_c == back_c


if __name__ == '__main__':
    S = Solution()
    N6 = ListNode(0)
    N5 = ListNode(2, N6)
    N4 = ListNode(3, N5)
    N3 = ListNode(3, N4)
    N2 = ListNode(2, N3)
    N1 = ListNode(1, N2)
    print(S.isPalindrome(N1))

