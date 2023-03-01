
def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    """
    This is an example of merging two sorted arrays, smart because you are just backfilling,

    You don't actually need to worry about the front because you are technically marking the front of the array
    think of the write_index as your return slice and slicing off the leftover beginning.

    However, I most likely don't fully understand how this is stored in memory, but it forces utilization of
    the full array.  I don't know if this could be a negative or how this is implemented in C.  Doesn't
    a basic array use null values at the end to designate the end of the array?  In the end the memory is
    allocated though, so the entire array is already 'in use' regardless of whether or not a portion just has
    zeroes/null or otherwise.
    """
    a, b, write_index = m-1, n-1, m + n - 1

    while b >= 0:
        if a >= 0 and A[a] > B[b]:
            A[write_index] = A[a]
            a -= 1
        else:
            A[write_index] = B[b]
            b -= 1

        write_index -= 1


class Solution:
    """
Return integer of
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):  # 1
            remaining = target - nums[i]  # 2

            if remaining in seen:  # 3
                return [i, seen[remaining]]  # 4
            else:
                seen[value] = i  # 5

#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        x = 1
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[x] = nums[i+1]
                x+=1
        return(x)

#https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

#https://leetcode.com/problems/search-insert-position/

def searchInsert(self, nums, target):
    """
    Input without duplicates
    :param self:
    :param nums:
    :param target:
    :return:
    """
    l , r = 0, len(nums)-1
    while l <= r:
        mid=(l+r)/2
        if nums[mid]== target:
            return mid
        if nums[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return l

def searchInsert(self, nums, target): # works even if there are duplicates.
    l , r = 0, len(nums)-1
    while l <= r:
        mid=(l+r)/2
        if nums[mid] < target:
            l = mid+1
        else:
            if nums[mid]== target and nums[mid-1]!=target:
                return mid
            else:
                r = mid-1
    return l

#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
def deleteDuplicates(self, head):
    cur = head
    while cur:
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next     # skip duplicated node
        cur = cur.next     # not duplicate of current node, move to next node
    return head

# https://leetcode.com/problems/sort-an-array/solutions/461394/python-3-eight-sorting-algorithms-with-explanation/?orderBy=most_votes&languageTags=python3

"""
Selection sort - O(n^2)
"""


class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L = len(N)
        return [N.pop(min(range(L - i), key=lambda x: N[x])) for i in range(L)]

"""
Bubble Sort - O(n^2)
"""
class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L, B = len(N), 1
        while B:
            B = 0
            for i in range(L-1):
                if N[i] > N[i+1]: N[i], N[i+1], B = N[i+1], N[i], 1
        return N

"""
Insertion Sort: - O(n^2)
"""

class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L = len(N)
        for i in range(1,L):
            for j in range(0,i):
                if N[i] < N[j]:
                    N.insert(j, N.pop(i))
                    break
        return N

"""
Binary Insertion Sort - O(n^2) - still necessary to go through entire list
"""


class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L = len(N)
        for i in range(1, L): bisect.insort_left(N, N.pop(i), 0, i)
        return N

"""
Counting Sort : O(n + k)
"""

class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        C, m, M, S = collections.Counter(N), min(N), max(N), []
        for n in range(m,M+1): S.extend([n]*C[n])
        return S

"""
Quicksort - worst case - O(n^2)
"""


class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        def quicksort(A, I, J):
            if J - I <= 1: return
            p = partition(A, I, J)
            quicksort(A, I, p), quicksort(A, p + 1, J)

        def partition(A, I, J):
            A[J - 1], A[(I + J - 1) // 2], i = A[(I + J - 1) // 2], A[J - 1], I
            for j in range(I, J):
                if A[j] < A[J - 1]: A[i], A[j], i = A[j], A[i], i + 1
            A[J - 1], A[i] = A[i], A[J - 1]
            return i

        quicksort(N, 0, len(N))
        return N

"""
Mergesort
"""
class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        def mergesort(A):
            LA = len(A)
            if LA == 1: return A
            LH, RH = mergesort(A[:LA // 2]), mergesort(A[LA // 2:])
            return merge(LH, RH)

        def merge(LH, RH):
            LLH, LRH = len(LH), len(RH)
            S, i, j = [], 0, 0
            while i < LLH and j < LRH:
                if LH[i] <= RH[j]:
                    i, _ = i + 1, S.append(LH[i])
                else:
                    j, _ = j + 1, S.append(RH[j])
            return S + (RH[j:] if i == LLH else LH[i:])

        return mergesort(N)

"""
Bucket Sort - O(n^2)
"""


class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        def insertion_sort(A):
            for i in range(1, len(A)):
                for j in range(0, i):
                    if A[i] < A[j]:
                        A.insert(j, A.pop(i))
                        break
            return A

        def bucketsort(A):
            buckets, m, S = [[] for _ in range(1000)], min(A), []
            R = max(A) - m
            if R == 0: return A
            for a in A: buckets[999 * (a - m) // R]
            for b in buckets: S.extend(insertion_sort(b))
            return S

        return bucketsort(N)