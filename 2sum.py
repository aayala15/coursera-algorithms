print("LOAD THE DATA")
data = set()
with open('2sum.txt', 'r') as f:
	for line in f:
		data.add(int(line))

def two_sum(nums):
	return(sum(sum(n - x in nums and 2*x != n for x in nums) for n in range(-10000, 10001)))

print(two_sum(data))