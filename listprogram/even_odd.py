lst1 = [1,2,3,4,5,6,7,8,9]
lst2 = []
lst3 = []
for i in lst1:
	if (i%2 == 0):
		lst2.append(i)
	else:
		lst3.append(i)
print lst2
print lst3
