"""
LeetCode 20. Valid Parenthese
Time: O(n)
Space: O(n)
Todo: clean up logic :)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {"()", "{}", "[]"}
        stack = []

        if s == "":
            return True

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
                continue
            if char in ")" or char == "}" or char == "]":
                if len(stack) == 0:
                    return False
                else:
                    if (stack[-1] + char) in valid_pairs:
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
