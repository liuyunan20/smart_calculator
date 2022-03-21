# process input to available parameters
def process_input(ipt):
    ipt = ipt.split()
    nums = []
    for x in ipt:
        try:
            x = int(x)
            nums.append(x)
        except ValueError:
            x = list(x)
            for j in x:
                if j not in ("+", "-"):
                    return None
            if x[0] == "-":
                if len(x) % 2 == 1:
                    nums.append("-")
            if x[0] == "+":
                nums.append("+")
    if len(nums) > 1 and "+" not in nums and "-" not in nums:
        return None
    for i, num in enumerate(nums):
        if i == len(nums) - 1 and num in ("+", "-"):
            return None
        if num == "-":
            nums[i] = 0
            nums[i + 1] = -nums[i + 1]
        if num == "+":
            nums[i] = 0
    return nums


help_information = '''The program operate addition and subtraction of numbers.
If the user has entered several same operators following each other, the program still work.
It support both unary and binary minus operators.'''
while True:
    user_in = input()
    if user_in.startswith("/") and user_in not in ("/exit", "/help"):
        print("Unknown command")
        continue
    if user_in == "/exit":
        print("Bye!")
        break
    if user_in == "/help":
        print(help_information)
        continue
    if not user_in:
        continue
    numbers = process_input(user_in)
    if numbers:
        print(sum(numbers))
    else:
        print("Invalid expression")
