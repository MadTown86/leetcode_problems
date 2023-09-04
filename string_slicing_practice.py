class Solution:
    def slice_show(self, inp: str) -> None:
        for x in range(len(inp)):
            print(f"{inp[x:]=} ::: {inp[:x]=} ::: {inp[-x:]=} ::: {inp[:-x]=}")

    def slice_replace(self, inp: str, i: int, j=int) -> str:
        res = ""
        res = inp[j] + inp[i:j] + inp[i] + inp[j:]
        return res


if __name__ == "__main__":
    S = Solution()
    input = ["12345", "22048", "12783333"]
    for x in input:
        print(S.slice_show(x))
        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                print(f"{i=} :::: {j=}")
                print(S.slice_replace(x, i, j))
