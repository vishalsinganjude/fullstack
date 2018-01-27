num = input("Enter Number: ")
temp = 0
for i in range (2,num):
    num1 = num%2
    temp = num
if (temp == 0):
    print("Num is not Prime.")
else:
    print("Num is prime.")
