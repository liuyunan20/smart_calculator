import re


def infix_to_postfix(expression):
    precedence = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2, "(": 3, ")": 3}
    result = []
    stack = []
    while expression:
        x = expression.pop(0)  # the current element in infix expression
        if x == "(":
            stack.append(x)
            continue
        if x == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            if not stack:
                return "Invalid expression"
            if stack[-1] == "(":
                stack.pop()
                continue
        if x not in ("+", "-", "*", "/", "^", "(", ")"):
            result.append(x)
            continue
        elif not stack or stack[-1] == "(":
            stack.append(x)
            continue
        elif precedence[stack[-1]] < precedence[x]:
            stack.append(x)
            continue
        else:
            while stack and precedence[stack[-1]] >= precedence[x]:
                if stack[-1] == "(":
                    break
                result.append(stack.pop())
            stack.append(x)
            continue
    if "(" in stack or ")" in stack:
        return "Invalid expression"
    while stack:
        result.append(stack.pop())
    return result


def process_input(ipt):
    variables = {}
    ipt = ipt.split()
    nums = []
    right_parenthesis = 0
    for x in ipt:
        if right_parenthesis == 1:
            nums.append(")")
            right_parenthesis = 0
        if x.startswith("("):
            nums.append("(")
            x = x.lstrip("(")
        if x.endswith(")"):
            x = x.rstrip(")")
            right_parenthesis = 1
        try:
            x = int(x)
            nums.append(x)
        except ValueError:
            if variables.get(x) is not None:
                nums.append(variables[x])
                continue
            if x.isalpha():
                return "Unknown variable"
            if re.fullmatch("\\++", x):
                nums.append("+")
            elif re.fullmatch("-+", x):
                nums.append("-") if len(x) % 2 == 1 else nums.append("+")
            elif x in ("*", "/", "^"):
                nums.append(x)
            else:
                return "Invalid identifier"
    if len(nums) > 1 \
            and "+" not in nums and "-" not in nums and "*" not in nums and "/" not in nums and "^" not in nums:
        return "Invalid expression"
    if nums[-1] in ("+", "-", "*", "/", "^", "("):
        return "Invalid expression"
    return nums


ex = "a*2+b*3+c*(2+3)"
print(process_input(ex))
