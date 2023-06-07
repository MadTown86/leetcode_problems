# https://leetcode.com/problems/palindrome-linked-list/

from collections import Counter
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def isPalindrome(self, head: ListNode) -> bool:

        #  Container to house linked list values to compare
        arr = []

        #  Incremental addition to arr until head == None and loop exit
        while head:
            arr.append(head.val)
            head = head.next

        #  Conditional cases for len <= 3
        #  There is an easier way to do this...
        if len(arr) <= 3:
            f, s, t = (arr[0], arr[1], arr[2]) if len(arr) == 3 else \
                (arr[0], arr[1], None) if len(arr) == 2 else (arr[0], None, None) if len(arr) == 1 else \
                    (None, None, None)

            if f is not None and s is not None and t is not None:
                if f == t:
                    return True
            elif f is not None and s is not None and t is None:
                if f == s:
                    return True
            elif f is not None and s is None and t is None:
                return True
            return False

        #  Typing reduction variable - house division of half
        #  Include center variable for odd sized list
        half = len(arr) // 2

        #  Create front half slice
        front = arr[:half]

        #  Create back half slice, add expression to alter for odd size
        if half * 2 < len(arr):
            back = arr[half + 1:]
        else:
            back = arr[half:]

        #  Reverse back in place
        back.reverse()

        print(front)
        print(back)

        #  Return the comparison
        return front == back

    def isPalindrome2(self, head: ListNode) -> bool:

        # I believe there can be a solution found by counting how many times a certain number is used and ensuring
        # it fits the palindrome rules

        cnt = Counter()
        while head:
            cnt[head.val] += 1
            head = head.next

        for item, val in cnt.items():
            print(item, val)

        return None

    def isPalindrome3(self, head: ListNode) -> bool:

        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        if len(arr) == 3:
            f, s, t = arr[0], arr[1], arr[2]
            if f == t and s != t:
                return True
            return False

        half = len(arr) // 2
        front = arr[:half]
        back = arr[half:]
        back.reverse()
        return front == back




if __name__ == '__main__':
    S = Solution()
    N6 = ListNode(0)
    N5 = ListNode(2, N6)
    N4 = ListNode(3, N5)
    N3 = ListNode(1, )
    N2 = ListNode(0, N3)
    N1 = ListNode(1, N2)
    print(S.isPalindrome3(N1))

