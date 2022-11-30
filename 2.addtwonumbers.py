"""
https://leetcode.com/problems/add-two-numbers/description/
"""

"""
First version of acceptable answer.  Because this problem had to do with linked lists and the core concept behind nodes
I felt I should try to finish it, despite it being a bit too much for me right now.  

I need to stop looking at leetcode when I tire of book reading...or I hope that this exercise, right after FIRST
reading about Linked lists and nodes sinks things into long-term memory.

A few takeaways just so I can hope to remember them the next time I run into these and also writing things in my
own words should help in retention and understanding, I hope...

First:  When LEETCODE questions give you a class definition you are supposed to use, DON'T entirely ignore it thinking
you have to write your own because they put an optional container class encapsulating it in their solution shell.
Despite this setback, it was good practice trying to conceptualize a queue/dequeue.

Second: Nodes are instances of a class that basically just have a data attribute and pointers towards next/previous
depending on queue or dequeue, etc.  The key here is that nothing is linking these other than the pointers.

You can assign variable names to certain nodes that you want to maintain access to after creation, such as creating 'header' and 'trailer' nodes or 
sentinel nodes.  This just aids in the ability to access and reassign pointers.  

When you add to a queue, a singly linked list, you keep a pointer towards the tail and a pointer towards the front.  What I 
mean by pointer in this context is a variable name assignment.  You assign the first node you create to a variable called
'first' or 'front' or 'head'.  Then the next node you create you assign to a variable name called 'tail'.  As you assign
the node to it, you also assign the 'front.next' attribute of the front node to the tail.

For some reason this next step was difficult for me to grasp and at times, I still kind of get mixed up.  So I want to 
analyze the following snip of code:

newest = ListNode(val, None)
tail.next = newest
tail = newest

For the longest time, I kept feeling like the tail = newest would somehow overwrite the pre-existing tail node but I 
need to remember that even normally, data elements that are created in this way are still in memory until garbage
collection even if the names assigned to them are suddenly used for other things.  I also need to remember that the
elements still have a reference assignment because each nodde references the next and so they won't be garbage collected.

A point on this would be, if I didn't have a 'front' node, there wouldn't be a way to access any of the other nodes and
they would all be garbage collected.

Essentially, you create a new node, point the pre-existing tail node instance variable .next to the new node in memory
and for quick reference only, you reassign the variable name 'tail' to the newest node you want at the end.

Python Answer - Leetcode Official:

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from itertools import zip_longest

class LinkedList:
    class Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, prev, nexter):
            self._element = element
            self._next = nexter

    def __init__(self):
        self._header = None
        self._second = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __next__(self):
        if self.is_empty():
            raise StopIteration
        return self.dequeue()

    def __iter__(self):
        return self

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            return None
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            return None
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, element):
        newest = self.Node(element, None, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def add_list(self, lister):
        while True:
            if lister.next != None:
                self.enqueue(lister.val)
                lister = lister.next
            else:
                self.enqueue(lister.val)
                break

class Solution:
    def addTwoNumbers(self, l1: LinkedList, l2:LinkedList) -> []:
        j = [0]
        front = None
        ntail = None
        L = LinkedList()
        L2 = LinkedList()
        L.add_list(l1)
        L2.add_list(l2)
        for x, y in zip_longest(L, L2, fillvalue=0):
            if j:
                v = x + y + j.pop()
            else:
                v = x + y
            if v >= 10:
                if not front and not ntail:
                    front = ListNode(v-10, None)
                elif not front.next:
                    ntail = ListNode(v-10, None)
                    front.next = ntail
                else:
                    newest = ListNode(v-10, None)
                    ntail.next = newest
                    ntail = newest
                j.append(1)
            else:
                if not front and not ntail:
                    front = ListNode(v, None)
                elif not front.next:
                    ntail = ListNode(v, None)
                    front.next = ntail
                else:
                    newest = ListNode(v, None)
                    ntail.next = newest
                    ntail = newest

        if j:
            if not ntail:
                ntail = ListNode(j.pop(), None)
                front.next = ntail
            else:
                newest = ListNode(j.pop(), None)
                ntail.next = newest
                ntail = newest
        return front



if __name__ == "__main__":
    S = Solution()
    testcase = [[1, 1, 1], [1, 1, 1]]
    testcase2 = [2, 4, 2], [8, 8, 8]
    testcase3 = [2, 3, 2, 3], [8, 9, 8]

    Y1 = ListNode(5, None)
    Y2 = ListNode(4, None)
    Y3 = ListNode(3, None)
    # Y1.next = Y2
    # Y2.next = Y3

    X1 = ListNode(5, None)
    X2 = ListNode(6, None)
    X3 = ListNode(4, None)
    # X1.next = X2
    # X2.next = X3


    LL1 = LinkedList()
    LL2 = LinkedList()
    crap = [0]
    crap2 = [0]
    for x in crap:
        LL1.enqueue(x)


    for y in crap2:
        LL2.enqueue(y)


    printit = S.addTwoNumbers(X1, Y1)

    while True:
        if printit.next != None:
            print(printit.val)
            printit = printit.next
        else:
            print(printit.val)
            break


