# https://leetcode.com/contest/weekly-contest-361/problems/minimum-operations-to-make-a-special-number/

import math


class Solution:
    def minimumOperations(self, num: str) -> int:
        """
        This solution was taken from the following:
        # https://leetcode.com/problems/minimum-operations-to-make-a-special-number/solutions/3995226/two-pointers-beats-100-python-submissions/

        Using this and creating explanation for each line of code to help memorize pattern for future use

        The nested for loop in this way allows you to check all possible arrangements.  I was originally using while
        loops and actually reducing the num value, which had added complexity and costs to time/memory than a
        comparison between res at each successful pair found.
        """
        # Create a dictionary with keys as values sought after by trailing pointer i
        pairs_dict = {"0": ["0", "5"], "5": ["2", "7"]}
        # Setting the trailing pointer default mark in case num is too small for nested range loop to reach jj
        jj = -1

        # Setting the trailing pointer default mark in case num is of length 1 or 0
        ii = -1

        # This is the interesting bit to remember, just using an infinite value in a min() to ensure never a
        # Clash takes place between a value you could choose off-hand as the 'highest' value to compare offhand
        # Perhaps it saves on memory to use this instead of using 1000000 or some other 'max' value
        res = math.inf

        # This for loop increments from the last position of num to num 0 and only proceeds to the next for loop
        # if it finds '0' or '5'
        for i in range(len(num) - 1, -1, -1):
            # This checks to see if the position of the 'i' pointer is either '0' or '5'
            if num[i] in pairs_dict.keys():
                # If True set ii to num[i] (0 or 5)
                ii = num[i]
                # This loops through all values from i-1 to 0 trying to find a specific pair by using the num[i] key
                for l in range(i - 1, -1, -1):
                    # This checks to see if num[l] can be found in pairs_dict[num[i]] = 0, 5 or 2, 7
                    if num[l] in pairs_dict[num[i]]:
                        # If it finds a pair then it sets jj to that value and avoids the final if-block
                        jj = num[l]
                        # Only when successful pairs are found will res be re-written
                        # The use of math.inf here as the original res value ensures that any value
                        # Of len(num)-l-2 will be smaller.
                        # len(num) - l gives you the amount of 'deleted' characters, offset by -1 because an array
                        # is indexed starting from 0 as normal, then offset by -1 again for a total of -2 because
                        # You are keeping the 'i' index value
                        res = min(res, len(num) - l - 2)

        # This line of code is executed if the second range 'for l in....' is never reached, meaning len(num) too small
        if jj == -1:
            # If the only value of num is 0, and this per the instructions is divisible by 25, then the min value
            # will be len(num)-1 which sets res to min(math.inf, 0): 0 < inf
            if ii == "0":
                res = min(res, len(num) - 1)
            # If the list was empty or just contains a '5' then this will return either a 0 or a 1
            if ii == -1 or ii == "5":
                # min(math.inf, len('') == 0 or len(1) for a value to be deleted)
                res = min(res, len(num))

        # Finally return the value of res
        return res


if __name__ == "__main__":
    S = Solution()
    inputs = ["2245047", "2908305", "10", "1", "11", "6525479784667", "2713539"]

    # assert S.minimumOperations(inputs[0]) == 2
    assert S.minimumOperations(inputs[1]) == 3
    assert S.minimumOperations(inputs[2]) == 1
    assert S.minimumOperations(inputs[3]) == 1
    assert S.minimumOperations(inputs[4]) == 2
    assert S.minimumOperations(inputs[5]) == 9
    assert S.minimumOperations(inputs[6]) == 4
