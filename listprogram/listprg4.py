def union(lst1,lst2):
	final_list = list(set(lst1) | set(lst2))
	return final_list
lst1 = [1,4,8,3,0]
lst2 = [4,3,2,7,9]
print (union(lst1,lst2))
