# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    stack = []

    for c in S:
        if c in "([{":
            stack.append(c)
        elif c in ")]}":
            if not stack:
                return 0
            bracket = stack.pop()
            if (bracket == '(' and c != ')' or
                bracket == '{' and c != '}' or
                bracket == '[' and c != ']'):
                return 0
    return 1 if not stack else 0

