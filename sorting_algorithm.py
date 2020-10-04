# Bubble sort
a = [3,6,4,8,1,5,9,2]
count = 0
for i in range(len(a)):
	for j in range(1, len(a)):
		if a[j-1] > a[j] :
			count = count +1
			a[j-1], a[j] = a[j], a[j-1]

print(a, count)			