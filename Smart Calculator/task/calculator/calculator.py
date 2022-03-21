while True:
    user_in = input()
    if user_in == "/exit":
        print("Bye!")
        break
    if user_in == "/help":
        print("The program calculates the sum of numbers")
        continue
    if not user_in:
        continue
    nums = [int(x) for x in user_in.split(" ")]
    print(sum(nums))
