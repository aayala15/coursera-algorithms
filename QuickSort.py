A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def GetMedian(A, l, r):
	m = int((r-l)/2+l)
	
	x = A[l]-A[m];
	y = A[m]-A[r];
	z = A[l]-A[r];
	if x*y > 0:
		p = m
	elif x*z > 0:
		p = r
	else:
		p = l
	return(p)

def Partition(A, l, r):
	# p = l # First element pivot
	# p = r # Last element pivot
	p = GetMedian(A, l, r) # Median element pivot
	
	A[p], A[l] = A[l], A[p]
	p = A[l]
	
	i = l + 1
	for j in range(l+1, r+1):
		if A[j] < p:
			A[i], A[j] = A[j], A[i]
			i += 1
	A[l], A[i-1] = A[i-1], A[l]
	return(i-1)

def QuickSort(A, l, r, count):
	if r > l:
		p = Partition(A, l, r)
		count[0] += r - l
		QuickSort(A, l, p-1, count)
		QuickSort(A, p+1, r, count)


# count = [0]
# QuickSort(A, 0, int(len(A))-1, count)
# print(A)
# print(count)

A = []
with open('QuickSort.txt', 'r') as f:
	for line in f:
		A.append(int(line))

count = [0]
QuickSort(A, 0, int(len(A))-1, count)
# print(A)
print(count)