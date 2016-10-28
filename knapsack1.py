import numpy as np

print("LOAD THE DATA")
items = []
with open('knapsack_big.txt', 'r') as f:
	data = str.split(f.readline())
	knapsack_size = int(data[0])
	number_of_items = int(data[1])
	for line in f:
		data = [int(a) for a in str.split(line)]
		items.append(data)

A = np.zeros([2, knapsack_size+1], dtype=np.int32)

for i in range(number_of_items):
	vi = int(items[i][0])
	wi = items[i][1]
	
	A[1,:wi] = A[0,:wi]
	A[1,wi:] = np.maximum(A[0,wi:], A[0,0:(knapsack_size-wi+1)] + vi)
	A[0,:] = A[1,:]

print(A)
print(A[1, knapsack_size])