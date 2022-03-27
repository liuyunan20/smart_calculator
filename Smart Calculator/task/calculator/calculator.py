import re


class Calculator:
    """create a Calculator object"""
    def __init__(self):
        self.operator = ("+", "-", "*", "/", "^", "(", ")")
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
            if x not in self.operator:
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

    # process input to available parameters
    def process_input(self, ipt):
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
                x = x.rsplit(")")
                right_parenthesis = 1
            try:
                x = int(x)
                nums.append(x)
            except ValueError:
                if self.variables.get(x) is not None:
                    nums.append(self.variables[x])
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
            numbers = self.process_input(user_in)
            if numbers == "Invalid expression":
                print("Invalid expression")
                continue
            if numbers == "Unknown variable":
                print("Unknown variable")
                continue
            if numbers == "Invalid identifier":
                print("Invalid identifier")
                continue
            print(sum(numbers))


cal = Calculator()
cal.calculate()
