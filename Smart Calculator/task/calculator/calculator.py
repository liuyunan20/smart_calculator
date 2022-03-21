while True:
    user_in = input()
    if user_in == "/exit":
        print("Bye!")
        break
    if not user_in:
        continue
    nums = [int(x) for x in user_in.split(" ")]
    print(sum(nums))
