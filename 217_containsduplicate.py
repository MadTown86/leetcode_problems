class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) < 22:
            l = []
            for x in nums:
                if x in l:
                    return True
                else:
                    l.append(x)
            return False
        else:

            l = sorted(nums)
            print(l)
            a, b, c, d, e, f = len(l) - 1, len(l) - 2, len(l) - 3, len(l) - 4, len(l) - 5, len(l) - 6
            t, u, v, x, y, z = 0, 1, 2, 3, 4, 5
            print(len(l))
            lastf = 0
            lastz = 0
            flag = True
            while t <= (len(l) // 2) + 6:
                if l[a] == l[b] or l[b] == l[c] or l[c] == l[d] or l[d] == l[e] or l[e] == l[f]:
                    lastf = l[f]
                    return True
                else:
                    a -= 5
                    b -= 5
                    c -= 5
                    d -= 5
                    e -= 5
                    f -= 5

                if l[t] ==l[u] or l[u] == l[v] or l[v] == l[x] or l[x] == l[y] or l[y] == l[z]:
                    return True
                else:
                    t += 6
                    u += 6
                    v += 6
                    x += 6
                    y += 6
                    z += 6

        return False


if __name__ == "__main__":
    test = [1, 2, 3, 1]
    test2 = [1, 2, 3, 4]
    test3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, ]
    test4 = [959, -123, 811, -940, 663, 560, 293, -180, 871, 794, 927, 135, 125, -583, 474, -834, -898, 912, 500, -158,
             -76, 260, 542, -716,
             320, 781, -413, -5, -899, 868, 899, 127, -739, -650, -32, -150, -296, -422, -390, -476, 514, 513, 337,
             -467, -168, 344, -511,
             -383, -10, 142, 370, -192, -754, -657, 318, -668, -846, -574, 26, 856, 663, 19, 128, -549, -72, 857, -318,
             555, -78, -124, -714, 122,
             -605, -500, -814, -642, -299, 139]
    s = Solution()
    print(s.containsDuplicate(test4))
