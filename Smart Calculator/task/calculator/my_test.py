import re
import string


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
    ipt = list(ipt.strip())
    if ipt[0] in ("+", "-", "*", "/", "^", ")") or ipt[-1] in ("+", "-", "*", "/", "^", "("):
        return "Invalid expression"
    exp = []  # expression
    while ipt:
        x = ipt.pop(0)
        operator = ""
        operand = ""
        if x in ("(", ")"):
            exp.append(x)
            continue
        while x in ("+", "-", "*", "/", "^"):
            operator += x
            if not ipt or ipt[0] not in ("+", "-", "*", "/", "^"):
                break
            x = ipt.pop(0)

        if operator:
            exp.append(operator)
            operator = ""
            continue
        while x in string.digits or x in string.ascii_letters:
            operand += x
            if not ipt or (ipt[0] not in string.digits and x not in string.ascii_letters):
                break
            x = ipt.pop(0)
        if operand:
            exp.append(operand)
            operand = ""
            continue
    if x == ")":
        exp.append(x)
    nums = []
    variables = {}
    for x in exp:
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
            elif x in ("*", "/", "^", "(", ")"):
                nums.append(x)
            else:
                return "Invalid identifier"
    if len(nums) > 1 \
            and "+" not in nums and "-" not in nums and "*" not in nums and "/" not in nums and "^" not in nums:
        return "Invalid expression"
    return nums


def cal_result(post_exp):
    stack = []
    for x in post_exp:
        if x in ("+", "-", "*", "/", "^"):
            opd_2 = stack.pop()
            opd_1 = stack.pop()
            if x == "+":
                stack.append(opd_1 + opd_2)
            if x == "-":
                stack.append(opd_1 - opd_2)
            if x == "*":
                stack.append(opd_1 * opd_2)
            if x == "/":
                stack.append(opd_1 / opd_2)
            if x == "^":
                stack.append(opd_1 ** opd_2)
            continue
        stack.append(x)
    print(stack)
    return stack[-1]


ex = "2^2"
print(process_input(ex))
print(infix_to_postfix(process_input(ex)))
print(cal_result(infix_to_postfix(process_input(ex))))
