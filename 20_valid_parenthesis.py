from time import perf_counter
class Solution:
    def is_valid(self, s: str) -> bool:
        o, c, i, stak = ['(', '{', '['], [')', '}', ']'], 0, []
        while i <= len(s)-1:
            if s[i] in o:
                stak.append(s[i])
                i += 1
                continue
            else:
                if not stak:
                    return False
                else:
                    if stak[-1] != o[c.index(s[i])]:
                        return False
                    else:
                        stak.pop()
                        i += 1
                        continue
        return True

    def is_valid2(self, s: str) -> bool:
        o, c, stak = ['(', '{', '['], [')', '}', ']'], []
        stak = []
        for i in range(len(s) - 1):
            if s[i] in o:
                stak.append(s[i])
                i += 1
                continue
            else:
                if not stak:
                    return False
                else:
                    if stak[-1] != o[c.index(s[i])]:
                        return False
                    else:
                        stak.pop()
                        i += 1
                        continue
        return True

    def is_valid3(self, s: str) -> bool:
        opp, stak = {"{": "}", "[": "]", "(": ")"}, []
        if len(s) < 2:
            return False
        for c in s:
            if c == '{' or c == '[' or c == '(':
                stak.append(c)
                continue
            else:
                if not stak:
                    return False
                else:
                    if c != opp[stak[-1]]:
                        return False
                    else:
                        stak.pop()
                        continue
        return True

    # Best Anser LeatCode:
    class Solution(object):
        def isValid(self, s):
            """
            :type s: str
            :rtype: bool
            """

            # The stack to keep track of opening brackets.
            stack = []

            # Hash map for keeping track of mappings. This keeps the code very clean.
            # Also makes adding more types of parenthesis easier
            mapping = {")": "(", "}": "{", "]": "["}

            # For every bracket in the expression.
            for char in s:

                # If the character is an closing bracket
                if char in mapping:

                    # Pop the topmost element from the stack, if it is non empty
                    # Otherwise assign a dummy value of '#' to the top_element variable
                    top_element = stack.pop() if stack else False

                    # The mapping for the opening bracket in our hash and the top
                    # element of the stack don't match, return False
                    if mapping[char] != top_element:
                        return False
                else:
                    # We have an opening bracket, simply push it onto the stack.
                    stack.append(char)

            # In the end, if the stack is empty, then we have a valid expression.
            # The stack won't be empty for cases like ((()
            return not stack

if __name__ == "__main__":
    S = Solution()
    t_inputs = ["()(())()[][]"*10000, "()[]{}"*20000, "(]"]

    def benchit(inp: str) -> str:
        start = perf_counter()
        S.is_valid(inp)
        stop = perf_counter()
        start2 = perf_counter()
        S.is_valid2(inp)
        stop2 = perf_counter()
        start3 = perf_counter()
        S.is_valid3(inp)
        stop3 = perf_counter()
        res = f'VAL1: {stop-start:.10f}, VAL2: {stop2-start2:.10f}, VAL3: {stop3-start3:.10f}'
        return res

    for inp in t_inputs:
        print(benchit(inp))

