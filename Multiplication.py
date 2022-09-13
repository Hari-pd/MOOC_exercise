num=int(input("please type in a number:"))
multiplier=1
while num>=multiplier:
    counter=1
    while num>=counter:
        print(f"{multiplier} x {counter} = {multiplier*counter}")
        counter+=1
    multiplier+=1