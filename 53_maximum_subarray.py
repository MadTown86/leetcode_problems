from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        p = [nums[0]]
        for k in nums[1:]:
            print(f'{p=}')
            if p[-1] + k > k:
                p.append(p[-1] + k)
            else:
                p.append(k)
        return max(p)

    def maxSubArray2(self, nums: List[int]) -> int:
        p = nums[0]
        c = nums[0]
        for k in nums[1:]:
            if p + k > k:
                p = p + k
            else:
                p = k
            if p > c:
                c = p
        return c




if __name__ == "__main__":
    S = Solution()

    # Situation 1 : all incrementing, no negatives
    # Situation 2 : mixed positives, no negatives
    # Situation 3 : Starts positive, mixed negative numbers but previous value never negative


    inputs = [[3, -1, 2], [3,-4, 1], [1, 2, 3]]

    """
    You can compare p[-1] to k, you can compare p[-1] + k
    """


    """
    You either keep p[-1], either keep k by shifting the start of the subarrray or add the summation
    
    
    """



    text1 = [-5, 1, -3, 4,-1,2,1,-5,4]
    text2 = [1]
    text3 = [5,4,-1,7,8]

    test = [-2, -1]

    for x in inputs:
        print(S.maxSubArray2(x))

    assert S.maxSubArray2(text1) == 6
    assert S.maxSubArray2(text2) == 1
    assert S.maxSubArray2(text3) == 23
    assert S.maxSubArray2(test) == -1
