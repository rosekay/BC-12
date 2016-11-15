# functiion that returns an array if the min and max numbers

def max_min(x):

	mini = maxi = x[0]

	for i in x[1:]:
		if i < mini:
			mini = i
		elif i > maxi:
			maxi = i
	return [mini, maxi]
				

	
print max_min([10, 12, -5, 6, 89, 30])
