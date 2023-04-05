class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    mirror = []
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        if head.next in self.mirror:
            return True
        else:
            self.mirror.append(head)
        return self.hasCycle(head.next)

"""
Not to pat myself on the back, but I felt like the only way to really make this 'faster' without more memory would be to
just catch an exception  of some sort.  Now I know that instead of just trying to let it loop and throw a 
'endless loop' exception and return the desired value there.

def hasCycle(self, head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False
"""

if __name__ == '__main__':
    N1 = ListNode(1)
    N2 = ListNode(2)
    N3 = ListNode(3)
    N4 = ListNode(4)
    N5 = ListNode(5)
    N6 = ListNode(6)
    N1.next = N2
    N2.next = N3
    N3.next = N4
    N4.next = N5
    N5.next = N6
    N6.next = N3
    S = Solution()
    print(S.hasCycle(N1))