def intersection(lst1,lst2):
	f_list = list(set(lst1) & set(lst2))
	return f_list 
lst1= [1,3,5,2,5,7,8,9]
lst2= [1,3,5,7,9,3,8]
print (intersection(lst1,lst2))
