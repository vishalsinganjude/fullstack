a = []
n = input("Enter number of elements: ")
for i in range(1,n+1):
	b = input("Enter a Element: ")
	a.append(b)
a.sort()
print a
print "Second largest Number is: ",a[n-2]
 
	

