number=int(input("Please type in a number:"))
starter=0
while starter<(number//2):
    print(f"{starter+1}\n{number-starter}")
    starter+=1
if number%2!=0:
    print(f"{(number//2)+1}")