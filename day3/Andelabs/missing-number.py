
# function to find the missing number from two arrays
def find_missing(list_one, list_two):
	
	missing_num = []

	
	if not list_one and not list_two:
		return 0
	if len(list_one) != len(list_two):
		for x in list_two:
			if x not in list_one:
				missing_num.append(x)
				return missing_num
				
	return 0	

print find_missing([1, 2, 3], [1, 2, 3, 4])
print find_missing([4, 66,7], [66, 77, 7, 4])