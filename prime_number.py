num = int(input("Write the number:- "))
if num <= 1:
    print("Not a prime")
else:
    for i in range(2,num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
         print("It is prime")


