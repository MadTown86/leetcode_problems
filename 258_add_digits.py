# https://leetcode.com/problems/add-digits/
class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) <= 1:
            return num
        elif len(str(num)) > 1:
            test = int(sum([int(x) for x in str(num)]))
            return self.addDigits(test)

if __name__ == "__main__":
    S = Solution()
    print(S.addDigits(181))

