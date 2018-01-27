num = input("Enter Num :")
for i in range(2,num):
    if(num%i==0):
        print("Not prime")
        break
    elif(num % i-1):
        print("prime")
        break