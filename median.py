import heapq

def main():
	msum = 0
	hlow = []
	hhigh = []
	with open('median.txt') as file_in:
		for line in file_in:
			num = int(line.strip())
			if len(hlow) == 0 or -hlow[0] >= num:
				heapq.heappush(hlow, -num)
			else:
				heapq.heappush(hhigh, num)
			
			if len(hlow) > len(hhigh) + 1:
				heapq.heappush(hhigh, -heapq.heappop(hlow))
			if len(hlow) < len(hhigh):
				heapq.heappush(hlow, -heapq.heappop(hhigh))
			msum += -hlow[0]
	print(msum % 10000)
	return([hlow, hhigh])


if __name__ == '__main__':
	result = main()
	print(result[0])
	print(result[1])