number = int (raw_input("Enter a number from 1 to 100: "))
for x in range(0,number + 1):
    if x % 3 == 0:
        print ("Fizz")
    elif x % 5 == 0:
        print ("Buzz")
    else:
        print (x)



