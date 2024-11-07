#25.	Write a program to Check for Balanced Parentheses using Stack

def isBalanced(exp: str) -> bool:
    stack = []
    bracket_pair = {')': '(', ']': '[', '}': '{'}
    for char in exp:
        if char in bracket_pair.values():
            stack.append(char)
        elif char in bracket_pair.keys():
            if  stack and stack[-1] == bracket_pair[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    exp = "((1+2)[a-b]){[d]}"
    print(isBalanced(exp))

