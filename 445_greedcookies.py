
def main(g: list, s: list)-> int:
    """
    input: two list arrays
    output: integer
    time complexity: linear
    """
    if not s:
        return 0
    s.sort()
    g.sort(reverse=True)
    a, res = 0, 0
    while a < len(g) and s:
        if s[-1] >= g[a]:
            s.pop()
            res += 1
        a += 1
    return res

if __name__ == "__main__":
    inputs = [([1, 2, 3], [1, 1]), ([1, 2], [1, 2, 3]), ([1, 2, 3], [3]), ([1, 2, 3], [])]
    for i in inputs:
        print(main(i[0], i[1]))