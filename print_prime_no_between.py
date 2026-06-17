num= int(input("Write the number where you need prime number between them:- "))
for i in range(2,num+1):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break
    else:
            print(i, end=" ")
            