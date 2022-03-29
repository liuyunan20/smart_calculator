import re
import string


class Calculator:
    """create a Calculator object"""
    def __init__(self):
        self.variables = {}
        self.precedence = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2, "(": 3, ")": 3}
        self.help_information = '''The program operate addition and subtraction of numbers.
If the user has entered several same operators following each other, the program still work.
It support both unary and binary minus operators.
Storing results in variables and then operating them at any time is a very convenient function.'''

    def infix_to_postfix(self, expression):
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
            if x not in ("+", "-", "*", "/", "^", ")", "("):
                result.append(x)
                continue
            elif not stack or stack[-1] == "(":
                stack.append(x)
                continue
            elif self.precedence[stack[-1]] < self.precedence[x]:
                stack.append(x)
                continue
            else:
                while stack and self.precedence[stack[-1]] >= self.precedence[x]:
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

    # process input to available parameters
    def process_input(self, ipt):
        ipt = list(ipt.strip())
        if ipt[0] in ("+", "*", "/", "^", ")") or ipt[-1] in ("+", "-", "*", "/", "^", "("):
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

        nums = []
        next_number_is_negative = False
        for x in exp:
            try:
                x = int(x)
                if next_number_is_negative:
                    nums.append(-x)
                    next_number_is_negative = False
                else:
                    nums.append(x)
            except ValueError:
                if next_number_is_negative:
                    return "Invalid expression"
                if self.variables.get(x) is not None:
                    nums.append(self.variables[x])
                    continue
                if x.isalpha():
                    return "Unknown variable"
                if x.isalnum():
                    return "Invalid identifier"
                if len(x) > 1 and x.endswith("-"):
                    x = x.rstrip("-")
                    next_number_is_negative = True
                if re.fullmatch("\\++", x):
                    nums.append("+")
                elif re.fullmatch("-+", x):
                    nums.append("-") if len(x) % 2 == 1 else nums.append("+")
                elif x in ("*", "/", "^", "(", ")"):
                    nums.append(x)
                else:
                    return "Invalid expression"
        if len(nums) > 1 and nums[0] == "-":
            nums.pop(0)
            nums[0] = -nums[0]
        if len(nums) > 1 \
                and "+" not in nums and "-" not in nums and "*" not in nums and "/" not in nums and "^" not in nums:
            return "Invalid expression"
        return nums

    def assign_variable(self, ipt):
        ipt = ipt.split("=")
        if ipt[0].strip().isalpha():
            if len(ipt) > 2:
                return "Invalid assignment"
            if ipt[1].strip().isdigit():
                self.variables[ipt[0].strip()] = int(ipt[1].strip())
            elif self.variables.get(ipt[1].strip()):
                self.variables[ipt[0].strip()] = self.variables[ipt[1].strip()]
            elif ipt[1].strip().isalpha():
                return "Unknown variable"
            else:
                return "Invalid assignment"
        else:
            return "Invalid identifier"

    def calculate(self):
        while True:
            user_in = input()
            if user_in.startswith("/") and user_in not in ("/exit", "/help"):
                print("Unknown command")
                continue
            if user_in == "/exit":
                print("Bye!")
                break
            if user_in == "/help":
                print(self.help_information)
                continue
            if not user_in:
                continue
            if "=" in user_in:
                variable = self.assign_variable(user_in)
                if variable == "Invalid identifier":
                    print("Invalid identifier")
                if variable == "Invalid assignment":
                    print("Invalid assignment")
                if variable == "Unknown variable":
                    print("Unknown variable")
                continue
            expression = self.process_input(user_in)
            # print(f"expression: {expression}")
            if expression == "Invalid expression":
                print("Invalid expression")
                continue
            if expression == "Unknown variable":
                print("Unknown variable")
                continue
            if expression == "Invalid identifier":
                print("Invalid identifier")
                continue
            post_expression = self.infix_to_postfix(expression)
            if post_expression == "Invalid expression":
                print("Invalid expression")
                continue
            # print(f"post_expression: {post_expression}")
            print(self.cal_result(post_expression))

    def cal_result(self, post_exp):
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
        # print(stack)
        return int(stack[-1])


cal = Calculator()
cal.calculate()
