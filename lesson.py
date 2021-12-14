# 20.Valid Parentheses
def isValid(self, s: str) -> bool:
    opening = "({["
    closing = ")}]"
    match = {
        '}': "{",
        "]": "[",
        ")": "("
    }

    stack = []
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False

            if stack[-1] == match[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0
