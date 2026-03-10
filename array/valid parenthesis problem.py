def isValid(s):
    stack = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if len(stack) == 0 or stack.pop() != mapping[char]:
                return False

    return len(stack) == 0


# Example
print(isValid("()[]{}"))   # True
print(isValid("(]"))       # False
print(isValid("([{}])"))   # True