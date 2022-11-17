class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) < 12:
            l = []
            for x in nums:
                if x in l:
                    return True
                else:
                    l.append(x)
            return False
        else:

            l = sorted(nums)
            a, b, c, d, e, f = len(l) - 1, len(l) - 2, len(l) - 3, len(l) - 4, len(l) - 5, len(l) - 6
            t, u, v, x, y, z = 0, 1, 2, 3, 4, 5

            while t <= (len(l) // 2) + 6:
                print(a, d, c, d, e, f)
                if l[a] == l[b] or l[b] == l[c] or l[c] == l[d] or l[d] == l[e] or l[e] == l[f]:
                    return True
                else:
                    a -= 6
                    b -= 6
                    c -= 6
                    d -= 6
                    e -= 6
                    f -= 6

                if t ==l[u] or l[u] == l[v] or l[v] == l[x] or l[x] == l[y] or l[y] == l[z]:
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
    test3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, ]
    s = Solution()
    print(s.containsDuplicate(test3))