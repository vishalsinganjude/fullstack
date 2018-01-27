def union(lst1,lst2):
	f_list = sorted(lst1+lst2)
	return f_list
lst1 = [9,8,7,6,5,4,3]
lst2 = [1,2,3,4,5,6,7]
print union(lst1,lst2)
