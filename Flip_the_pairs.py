num=int(input("Please type in a number:"))
starting_num=2
while True:
    if starting_num==num:
        print(starting_num)
        print(starting_num-1)
        break
    elif starting_num>num:
        print(starting_num-1)
        break
    print(f"{starting_num}\n{starting_num-1}")
    starting_num+=2