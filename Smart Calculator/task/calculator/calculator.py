class Calculator:
    """create a Calculator object"""
    def __init__(self):
        self.variables = {}
        self.help_information = '''The program operate addition and subtraction of numbers.
If the user has entered several same operators following each other, the program still work.
It support both unary and binary minus operators.
Storing results in variables and then operating them at any time is a very convenient function.'''

    # process input to available parameters
    def process_input(self, ipt):
        ipt = ipt.split()
        nums = []
        for x in ipt:
            try:
                x = int(x)
                nums.append(x)
            except ValueError:
                if self.variables.get(x) is not None:
                    nums.append(self.variables[x])
                    continue
                if x.isalpha():
                    return "Unknown variable"
                x = list(x)
                for j in x:
                    if j not in ("+", "-"):
                        return "Invalid identifier"
                if x[0] == "-":
                    if len(x) % 2 == 1:
                        nums.append("-")
                if x[0] == "+":
                    nums.append("+")
        if len(nums) > 1 and "+" not in nums and "-" not in nums:
            return "Invalid expression"
        for i, num in enumerate(nums):
            if i == len(nums) - 1 and num in ("+", "-"):
                return "Invalid expression"
            if num == "-":
                nums[i] = 0
                nums[i + 1] = -nums[i + 1]
            if num == "+":
                nums[i] = 0
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
