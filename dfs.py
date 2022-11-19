def checkPair(exp):
    stack = []

    for ch in exp:
        if ch not in "()":
            continue
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack:
                return False
            stack.pop()
        else:
            return False

    # return not stack
    return True


if __name__ == "__main__":
    expressions = ["( ( ( ) ) ", "( ) ) ( ( )	", "( ( ) ( ) ) )", "( ( ) ) ) ( )"]
    expressions = ["( ( ) ( ) ) )"]

    for exp in expressions:
        if checkPair(exp):
            print(f"{exp} \n=> 수식의 괄호가 바르게 사용되었습니다.")
        else:
            print(f"{exp} \n=> 수식의 괄호가 잘못 사용되었습니다.")