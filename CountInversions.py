A = [1,2,5,5,5,6,7,8,10]

def MergeCountSplitInv(B, C, n):
	i = 0
	j = 0
	count = 0
	D = []
	for a in range(n):
		if j>=len(C) or (i<len(B) and B[i] <= C[j]):
			D.append(B[i])
			i += 1
		else:
			D.append(C[j])
			j += 1
			count += len(B) - i
	return([D, count])

def SortCountInv(A, n):
	if n == 1:
		count = 0
		return([A, count])
	else:
		nhalf = int(n/2)
		B, x = SortCountInv(A[:nhalf], nhalf)
		C, y = SortCountInv(A[nhalf:], len(A)-nhalf)
		D, z = MergeCountSplitInv(B, C, n)
		return([D, x+y+z])

SortedA, CountInv = SortCountInv(A, int(len(A)))
print(SortedA)
print(CountInv)

result = 0
array = []
with open('IntegerArray.txt', 'r') as f:
	for line in f:
		array.append(int(line))
	SortedA , CountInv = SortCountInv(array, int(len(array)))
	print("Final result %s"%(CountInv))
	print(SortedA)


