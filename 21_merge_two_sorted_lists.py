from collections import deque
class ListNode:
    __slots__ = 'val', 'next'
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
class Solution:

    """
    This one works, last one is a re-write from a discussion post.  I hit a wall this time because I didn't know
    additional basic functionality of the ListNode construct.

    First - I didn't realize that ListNode has basic 'is_empty()' functionality when used in a conditional statement.
    'if list1' I assumed would throw an error or even comparison.  I wonder how it determines which instance attributes
    to compare if there are multiple.

    Second - because of this I didn't know how to mimic their test answers because I always tried to use the .value
    attribute, which always defaulted to 0 as written by their code snippet.  How would you then show an empty linked
    list.

    Third - I need to remember that when working with linked lists, the entirety is basically references.  Meaning,
    you just need to change the pointers around to rearrange something.  It was never necessary to 'build' anything
    separately.
    """
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2

        d = []
        list3 = ListNode()
        head = ListNode(next=list3)


        d.append(list1.val)
        while list1.next is not None:
            d.append(list1.next.val)
            list1 = list1.next

        d.append(list2.val)
        while list2.next is not None:
            d.append(list2.next.val)
            list2 = list2.next

        d.sort(reverse=True)
        list3 = ListNode()
        head = ListNode(val=d.pop(), next=list3)

        while len(d) > 1:
            list3.val = d.pop()
            list3.next = ListNode()
            list3 = list3.next
        list3.val = d.pop()

        return head

    # Test after viewing an answer:  Remember, just changing pointers
    def mergeTwoLists2(self, list1: ListNode, list2: ListNode) -> ListNode:
        # if not list1 and not list2:
        #     return list1
        # if not list1 or not list2:
        #     return list1 if not list2 else list2

        dummy = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1, dummy = list1.next, list1
            else:
                dummy.next = list2
                list2, dummy = list2.next, list2

        if list1 or list2:
            dummy.next = list1 if list1 else list2

        return head.next


    """
    class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2
        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = seek
        while seek and target:
            while seek.next and seek.next.val < target.val:
                seek = seek.next
            seek.next, target = target, seek.next
            seek = seek.next
        return head
    """


if __name__ == "__main__":
    S = Solution()
    L5 = ListNode(1)
    L4 = ListNode(2, next=L5)
    L3 = ListNode(3, next=L4)
    L2 = ListNode(4, next=L3)
    L1 = ListNode(5, next=L2)

    R5 = ListNode(5)
    R4 = ListNode(4, next=R5)
    R3 = ListNode(3, next=R4)
    R2 = ListNode(2, next=R3)
    R1 = ListNode(1, next=R2)

    F1 = ListNode()
    F2 = ListNode()

    objss = S.mergeTwoLists(F1, F2)

    print(objss.val)
    while objss.next is not None:
        print(objss.next.val)
        objss = objss.next









