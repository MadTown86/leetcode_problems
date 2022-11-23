"""
https://leetcode.com/problems/two-sum/?envType=study-plan&id=data-structure-i
"""

# Question didn't specify whether you could sort the list
class Solution:
    # If you can find it in one pass, great, otherwise accumulate lower values to separate list
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sort_nums = [x for x in enumerate(nums)]
        sort_nums.sort(key=lambda x: x[1])
        step = 0
        low = 0
        find = None
        lastfind = 0
        h = len(nums) - 1
        m = (low + h) // 2
        while step < len(nums):
            low = step
            h = len(nums) - 1
            m = (low + h) // 2
            if target == 0 and nums.count(0) >= 2:
                lastfind = find
                find = 0
                if find == lastfind:
                    step += 1
                    continue
                while sort_nums[m][1] != find and h - low > 1:
                    if find < sort_nums[m][1]:
                        h = m
                        m = (low + h) // 2
                    elif find > sort_nums[m][1]:
                        low = m
                        m = (low + h) // 2
                if sort_nums[m][1] == find:
                    return [sort_nums[step][0], sort_nums[m][0]]
                else:
                    step += 1
            if target == 0:
                lastfind = find
                find = sort_nums[step][1] * -1
                if find == lastfind:
                    step += 1
                    continue
                while sort_nums[m][1] != find and h - low > 1:
                    if find < sort_nums[m][1]:
                        h = m
                        m = (low + h) // 2
                    elif find > sort_nums[m][1]:
                        low = m
                        m = (low + h) // 2
                if sort_nums[m][1] == find:
                    return [sort_nums[step][0], sort_nums[m][0]]
                else:
                    step += 1
            if 0 > target > sort_nums[step][1]:
                lastfind = find
                find = sort_nums[step][1] - target
                if find == lastfind:
                    step += 1
                    continue
                while sort_nums[m][1] != find and h-low > 1:
                    if find < sort_nums[m][1]:
                        h = m
                        m = (low + h) // 2
                    elif find > sort_nums[m][1]:
                        low = m
                        m = (low + h) // 2
                if sort_nums[m][1] == find:
                    return [sort_nums[step][0], sort_nums[m][0]]
                else:
                    step += 1
            elif 0 > target < sort_nums[step][1]:
                lastfind = find
                find = sort_nums[step][1] - target
                if find == lastfind:
                    step += 1
                    continue
                while sort_nums[m][1] != find and h-low > 1:
                    if find < sort_nums[m][1]:
                        h = m
                        m = (low + h) // 2
                    elif find > sort_nums[m][1]:
                        low = m
                        m = (low + h) // 2
                if sort_nums[m][1] == find:
                    return [sort_nums[step][0], sort_nums[m][0]]
                else:
                    step += 1
            elif 0 < target > sort_nums[step][1]:
                lastfind = find
                find = target - sort_nums[step][1]
                if find == lastfind:
                    step += 1
                    continue
                while sort_nums[m][1] != find and h-low > 1:
                    if find < sort_nums[m][1]:
                        h = m
                        m = (low + h) // 2
                    elif find > sort_nums[m][1]:
                        low = m
                        m = (low + h) // 2
                if sort_nums[m][1] == find:
                    return [sort_nums[step][0], sort_nums[m][0]]
                else:
                    step += 1
            elif 0 < target < sort_nums[step][1]:
                lastfind = find
                find = target - sort_nums[step][1]
                if find == lastfind:
                    step += 1
                    continue
                while sort_nums[m][1] != find and h-low > 1:
                    if find < sort_nums[m][1]:
                        h = m
                        m = (low + h) // 2
                    elif find > sort_nums[m][1]:
                        low = m
                        m = (low + h) // 2
                if sort_nums[m][1] == find:
                    return [sort_nums[step][0], sort_nums[m][0]]
                else:
                    step += 1

if __name__ == "__main__":
    S = Solution()
    testcase = ([2, 4, 21, 33, 2, 16, 6, 13, 1, 1, 11, 5], 16)
    testcase2 = ([5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5], 10)
    testcase3 = ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1)
    testcase4 = ([0, 4, 3, 0], 0)
    print(S.twoSum(*testcase2))