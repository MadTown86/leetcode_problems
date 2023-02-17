
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